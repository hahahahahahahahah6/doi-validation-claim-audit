import json
import os
from pathlib import Path
import tempfile
import unittest
from doi_validation_claim_audit.audit import audit, claims, evidence, main
from doi_validation_claim_audit.phrases import DOIVALIDATION, NODOIVALIDATION, GENERIC_NAMES

class AuditTests(unittest.TestCase):
    def test_claims(self):
        for phrase in DOIVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NODOIVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        for text, expected in [('documented doi validation claim false',(True,False)),('doi validation claim audit',(True,False)),('documented no doi validation claim false',(False,True)),("doesn't validate-doi",(False,True)),('```\nvalidate doi\n```',(False,False)),('`validate doi`',(True,False)),('no doi validation and check doi',(True,True))]:
            with self.subTest(text=text): self.assertEqual(claims(text),expected)

    def test_routes(self):
        for source in ['from idutils import is_doi\nis_doi(x)', 'from idutils import is_doi as d\nd(x)', 'import idutils\nidutils.is_doi(x)', 'import idutils as iu\niu.is_doi(x)']:
            with self.subTest(source=source): self.assertTrue(evidence(source))
        for name in GENERIC_NAMES:
            for source in ['obj.'+name+'(x)', 'from other import '+name+'\n'+name+'(x)', 'from other import '+name+' as f\nf(x)']:
                with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_non_evidence(self):
        cases=['import idutils', 'is_doi(x)', 'x.is_doi(x)', 'validate_doi(x)', 'import subprocess\nsubprocess.run(["validate_doi"])', '"validate doi"\n# idutils.is_doi(x)', 'import idutils\nidutils = 3\nidutils.is_doi(x)', 'from idutils import is_doi\nis_doi = 3\nis_doi(x)', 'import idutils\nidutils.is_doi(', 'len(x)', '"/" in x', 'x.startswith("doi:")', 'import idutils\nidutils.doi_regexp.match(x)', 'import idutils\nidutils.doi_regexp.search(x)']
        for name in 'normalize_doi to_url is_handle is_ark is_urn is_arxiv is_arxiv_post_2007 is_arxiv_pre_2007 is_pmid is_pmcid is_istc is_cstr is_ean is_ean13 is_ean8 is_email is_url is_orcid is_isni is_isbn is_isbn10 is_isbn13 is_issn is_gnd is_hal is_ror is_rrid is_swh is_viaf is_wikidata is_openalex'.split(): cases.append('import idutils\nidutils.'+name+'(x)')
        for name in 'validate_doi get_real_url_from_doi find_doi_in_text pdf_to_doi get_clean_doi'.split():
            cases.extend(['import doi\ndoi.'+name+'(x)', 'from doi import '+name+' as f\nf(x)'])
        for module,names in [('pydoi',['resolve','get_url']),('validators',['doi','validate_doi']),('stdnum',['validate_doi']),('re',['match','search','fullmatch'])]:
            for name in names: cases.append('import '+module+'\n'+module+'.'+name+'(x)')
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))
        self.assertFalse(evidence('import idutils'))
        self.assertFalse(evidence('idutils.is_doi(x)'))

    def test_scope_and_exclusions(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate doi')
            for folder in ['fixtures','docs','examples']:
                (p/folder).mkdir(); (p/folder/'a.py').write_text('import idutils\nidutils.is_doi(x)')
            (p/'a.py').write_text('import idutils'); (p/'b.py').write_text('idutils.is_doi(x)')
            (p/'link.py').symlink_to(p/'fixtures/a.py')
            self.assertEqual(audit(p)[0]['severity'],'HIGH')
            (p/'tests').mkdir(); (p/'tests/test_a.py').write_text('import idutils\nidutils.is_doi(x)')
            self.assertEqual(audit(p)[0]['severity'],'MEDIUM')
            (p/'a.py').write_text('import idutils\nidutils.is_doi(x)')
            self.assertEqual(audit(p),[])
            (p/'README.md').write_text('no doi validation')
            self.assertEqual(audit(p)[0]['severity'],'HIGH')
            self.assertEqual(audit(p,['a.py']),[])

    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); (p/'README.md').write_text('validate doi'); (p/'test_a.py').write_text('import idutils\nidutils.is_doi(x)')
            self.assertEqual(main(['audit',d]),0)
            self.assertEqual(main(['audit',d,'--fail-on','medium','--json']),2)
            self.assertEqual(main(['audit',d,'--ignore','README.md','--verbose']),0)
            self.assertEqual(main(['audit',str(p/'absent')]),1)
            with self.assertRaises(SystemExit) as cm: main(['--version'])
            self.assertEqual(cm.exception.code,0)

    def test_shadowing(self):
        for source in ['def validate_doi(x): pass\na.validate_doi(x)', 'import thing as t\nt = 1\nt.validate_doi(x)', 'from other import validate_doi\nwith x as validate_doi: pass\nvalidate_doi(x)']:
            with self.subTest(source=source): self.assertFalse(evidence(source))
        self.assertTrue(evidence('x = object()\nx.validate_doi(v)'))
