# DOI claim audit

An offline static audit compares documented digital-object-identifier claims with Python source calls. It does not run source code or access the network.

## Usage

```sh
doi-validation-claim-audit audit .
python3 -m doi_validation_claim_audit audit . --json
doi-validation-claim-audit audit . --fail-on medium --ignore vendor
doi-validation-claim-audit --version
```

A positive claim without production evidence produces a high finding, or a medium finding when evidence exists only in tests. A negative claim with production evidence produces a high finding. Exit status is 0 for a pass, 2 at the selected threshold, and 1 for an input or usage error.

```
documented-doi-validation-claim-false
documented-no-doi-validation-claim-false
```

The idutils predicate returns a match object or None, rather than a boolean. The similarly named operation in the doi package performs network resolution and is not counted.

## Limitations

A normalisation call strips a leading scheme and never judges a string.

A conversion call builds a resolver address and never judges a string.

A resolution call asks the network whether a string is registered.

An extraction call reads a string out of text and never judges it.

A cleaning call rewrites separators and never judges a string.

A direct pattern match is a shape check, not a library judgement.

A Handle call judges a wider namespace and is not recognised.

An arXiv call judges a preprint string and is not recognised.

A PMID call judges a medical record string and is not recognised.

The validators package does not provide the relevant route.

The stdnum package does not provide the relevant route.

Strings, comments, imports and bare references do not establish a call.

Syntax errors prevent source evidence.

Calls split across modules do not combine into evidence.

A subprocess invocation does not count.

Roadmap, changelog and TODO prose can produce claims without implemented code.

The library does not establish registration of any string.

There is no check digit: any string matching the shape passes.

A space inside the tail passes the shape check.

A trailing space passes the shape check.

A trailing newline passes the shape check.

An embedded newline fails the shape check.

A leading space fails the shape check.

A missing tail fails: 10.1000/ is rejected.

A leading 9 fails: 9.1000/xyz123 is rejected.

An empty string fails the shape check.

Uppercase letters pass: DOI:10.1000/XYZ123 is accepted.

A resolver address form passes: https://doi.org/10.1000/xyz123 is accepted.

A bare scheme form passes: doi:10.1000/xyz123 is accepted.

A single-character slip in the tail still passes the shape check.

## Matched phrases

```
validate doi
validates doi
validating doi
doi validation
doi validations
doi validator
doi validation check
doi check
check doi
verify doi
doi verification
doi is valid
doi is invalid
valid doi
invalid doi
doi validity
doi format validation
validate doi format
doi length validation
doi character validation
is valid doi
is doi valid
doi validation library
doi validation function
doi validation tool
checks doi
checking doi
verifies doi
verifying doi
validate digital object identifier
validates digital object identifier
validating digital object identifier
digital object identifier validation
digital object identifier validations
digital object identifier validator
digital object identifier validation check
digital object identifier check
check digital object identifier
verify digital object identifier
digital object identifier verification
digital object identifier is valid
digital object identifier is invalid
valid digital object identifier
invalid digital object identifier
digital object identifier validity
digital object identifier format validation
validate digital object identifier format
is valid digital object identifier
is digital object identifier valid
digital object identifier validation library
no doi validation
does not validate doi
no doi validator
no doi validation check
does not support doi validation
without doi validation
doi validation not supported
doi validation not available
cannot validate doi
cannot check doi
does not check doi
no doi check
does not verify doi
no doi verification
doi validation not implemented
does not validate doi format
no digital object identifier validation
does not validate digital object identifier
no digital object identifier validator
digital object identifier validation not supported
cannot validate digital object identifier
does not verify digital object identifier
no digital object identifier verification
digital object identifier validation not implemented
```

```
doi
digital object identifier
doi.org
registrant
suffix
prefix
identifier
handle
```

```
validate doi
```

The bare phrase above can describe a manual runbook step.

```
doi validation
```

The bare phrase above can describe a roadmap feature.

```
doi validator
```

The bare phrase above can describe a hosted web page.

```
doi check
```

The bare phrase above can describe a field-presence lint rule.

```
check doi
```

The bare phrase above can describe a manual runbook step.

```
verify doi
```

The bare phrase above can describe a visual account confirmation.

```
doi validation check
```

The bare phrase above can describe a field-presence check.

```
valid doi
```

The bare phrase above can appear as example output.

```
doi is valid
```

The bare phrase above can appear as example error text.

```
doi is invalid
```

The bare phrase above can name a configuration flag or column.

```
doi validity
```

The bare phrase above can describe a format without code.

```
doi format validation
```

The bare phrase above can describe a shape-only check.

```
validate doi format
```

The bare phrase above can name a specification section.

```
digital object identifier validation
```

The bare phrase above can describe a manual runbook step.

```
validate digital object identifier
```

The bare phrase above can describe a manual runbook step.

```
check digital object identifier
```

The bare phrase above can describe a manual runbook step.

```
verify digital object identifier
```

The bare phrase above can name a specification section.

```
digital object identifier check
```

The bare phrase above can name a reference-data checklist item.

```
digital object identifier validation check
```

The bare phrase above can describe a result from an external platform.

```
digital object identifier validator
```

The bare phrase above alone names a string without judging it.

```
doi
```

The bare phrase above alone does not claim a judgement.

```
digital object identifier
```

The bare phrase above alone does not claim a judgement.

```
doi.org
```

The bare phrase above alone does not claim a judgement.

```
registrant
```

The bare phrase above alone does not claim a judgement.

```
suffix
```

The bare phrase above alone does not claim a judgement.

```
prefix
```

The bare phrase above alone does not claim a judgement.

```
identifier
```

The bare phrase above alone does not claim a judgement.

```
handle
```

The bare phrase above alone does not claim a judgement.

## Differentiation

This audit does not cover resolving a string over the network (the resolution family).

This audit does not cover reading a string out of text or a document (the extraction family).

This audit does not cover judging whether a string is a well-formed expanded-name string (the expanded-name family — the same judgement under its expanded name, an alias of this family's judgement, listed here so the overlap is explicit rather than hidden).

This audit does not cover checking whether a string is a well-formed handle-system string (the handle family).

This audit does not cover checking whether a string is a well-formed archival resource key (the ark family).

This audit does not cover checking whether a string is a well-formed uniform resource name (the urn family).

This audit does not cover checking whether a string is a well-formed preprint string (the arxiv family).

This audit does not cover checking whether a string is a well-formed medical record string (the pmid family).

This audit does not cover checking whether a string is a well-formed open-access record string (the pmcid family).

This audit does not cover checking whether a string is a well-formed text-content string (the istc family).

This audit does not cover checking whether a string is a well-formed science-resource string (the cstr family).

This audit does not cover checking whether a string is a well-formed research-organisation string (the ror family).

This audit does not cover checking whether a string is a well-formed openalex string (the openalex family).

This audit does not cover checking whether a string is a well-formed authority-file string (the viaf family).

This audit does not cover checking whether a string is a well-formed wikidata string (the wikidata family).

This audit does not cover checking whether a string is a well-formed authority record string (the gnd family).

This audit does not cover checking whether a string is a well-formed archive string (the hal family).

This audit does not cover checking whether a string is a well-formed software-heritage string (the swh family).

This audit does not cover checking whether a string is a well-formed research-resource string (the rrid family).

This audit does not cover checking whether a string is a well-formed six-letter classification string (the cfi family).

This audit does not cover checking whether a creditor-reference string is well-formed (the creditor-reference family).

This audit does not cover reading a classification string out of a document (the classification-code-extraction family).

This audit does not cover looking a string up by its classification code (the classification-code-lookup family).

This audit does not cover assigning a new classification code to a string (the classification-code-assignment family).

This audit does not cover checking whether input is checked at all (the generic validation family).

This audit does not cover checking whether a book number passes the ISBN-10 / ISBN-13 check digit (the ISBN-validation family — an ISBN-13 is a 13-digit decimal book number, and only a string starting with "10." tells a DOI apart).

This audit does not cover checking whether a serial number passes the ISSN check digit (the ISSN-validation family).

This audit does not cover checking whether a bank account number passes the IBAN check digit (the IBAN-validation family).

This audit does not cover checking whether a universally unique identifier string is well-formed (the UUID-validation family).

This audit does not cover checking whether a version string is a well-formed semantic version (the semver-validation family).

This audit does not cover checking whether a hardware address string is well-formed (the MAC-address-validation family).

This audit does not cover checking whether a business identifier code string is well-formed (the BIC-validation family).

This audit does not cover checking whether a cron-expression string is well-formed (the cron-expression-validation family).

This audit does not cover turning a cron-expression string into a human-readable sentence (the cron-expression-description family).

This audit does not cover checking whether anything runs on a schedule (the scheduled-execution family).

This audit does not cover checking whether a date string is well-formed (the date-validation family).

This audit does not cover checking whether a call times out (the timeout family).

This audit does not cover checking whether a payment is processed (the payment-processing family).

This audit does not cover reading a card number out of a document (the credit-card-extraction family).

This audit does not cover checking whether a user is authenticated (the auth family).

This audit does not cover hashing a password (the password-hashing family).

This audit does not cover generating a password (the password-generation family).

This audit does not cover encrypting a PDF (the PDF-encryption family).

This audit does not cover sending an email (the email-sending family).

This audit does not cover sending a text message (the SMS-sending family).

This audit does not cover reading data out of a document (the document-extraction family).

This audit does not cover scanning a barcode (the barcode-scanning family).

This audit does not cover checking whether an email address is well-formed (the email-validation family).

This audit does not cover checking whether a phone number is well-formed (the phone-validation family).

This audit does not cover checking whether a password is strong (the password-strength family).

This audit does not cover checking whether a document matches a JSON Schema (the JSON-Schema-validation family).

This audit does not cover checking whether a card number is well-formed (the credit-card-validation family).

This audit does not cover checking whether a domain name is well-formed (the domain-validation family).

This audit does not cover checking whether a URL is well-formed (the URL-validation family).

This audit does not cover checking whether an IP address is well-formed (the IP-validation family).

This audit does not cover parsing JSON (the JSON-parsing family).

This audit does not cover matching a regular expression (the regex family).

This audit does not cover parsing a URL (the URL-parsing family).

This audit does not cover fetching a URL (the URL-fetching family).

This audit does not cover resolving a domain name (the DNS family).

This audit does not cover generating a barcode (the barcode-generation family).

This audit does not cover reading an account number out of a document (the account-extraction family).

This audit does not cover reading a vehicle identification number out of a document (the VIN-extraction family).

This audit does not cover decoding a vehicle identification number (the VIN-decoding family).

This audit does not cover looking up a vehicle identification number's history (the VIN-history-lookup family).

This audit does not cover checking whether a hex color string is well-formed (the hex-color-validation family).

This audit does not cover checking whether a researcher identifier string is well-formed (the ORCID-validation family).

This audit does not cover checking whether a name identifier string is well-formed (the ISNI-validation family).

This audit does not cover checking whether a chemical registry number string is well-formed (the CASRN-validation family).

This audit does not cover checking whether a stock-exchange identifier string is well-formed (the SEDOL-validation family).

This audit does not cover checking whether a securities identifier string is well-formed (the ISIN-validation family).

This audit does not cover looking up a securities identifier's record (the ISIN-record-query family).

This audit does not cover reading a securities identifier out of a document (the ISIN-extraction family).

This audit does not cover checking whether a security identifier string is well-formed (the CUSIP-validation family — a CUSIP is a 9-character security identifier with a mod-10 check digit, and judging one says nothing about a DOI).

This audit does not cover checking whether a device identifier string is well-formed (the IMEI-validation family).

This audit does not cover checking whether a mobile equipment identifier string is well-formed (the MEID-validation family).

This audit does not cover checking whether a legacy mobile equipment identifier string is well-formed (the ESN-validation family).

This audit does not cover checking whether a music number string is well-formed (the ISMN-validation family).

This audit does not cover checking whether an audiovisual number string is well-formed (the ISAN-validation family).

This audit does not cover checking whether a release identifier string is well-formed (the GRid-validation family).

This audit does not cover checking whether a barcode number string is well-formed (the EAN-validation family).

This audit does not cover checking whether a serial number string is well-formed (the generic-serial-number family).

This audit does not cover checking whether a financial instrument identifier string is well-formed (the FIGI-validation family).

This audit does not cover looking up a financial instrument identifier's record (the FIGI-record-query family).

This audit does not cover reading a financial instrument identifier out of a document (the FIGI-extraction family).

This audit does not cover checking whether a recording code string is well-formed (the ISRC-validation family).

This audit does not cover checking whether an Ethereum address string is well-formed (the Ethereum-address-validation family).

This audit does not cover checking whether a Binance Smart Chain address string is well-formed (the Binance-Smart-Chain-address-validation family).

This audit does not cover checking whether a Tron address string is well-formed (the Tron-address-validation family).

This audit does not cover checking whether a Litecoin address string is well-formed (the Litecoin-address-validation family).

This audit does not cover checking whether a Dogecoin address string is well-formed (the Dogecoin-address-validation family).

This audit does not cover checking whether a bitcoin address string is well-formed (the bitcoin-address-validation family).

This audit does not cover checking whether a transaction hash string is well-formed (the transaction-hash-validation family).

This audit does not cover checking whether a private key string is well-formed (the private-key-validation family).

This audit does not cover looking up a balance or transactions on a block explorer (the block-explorer family).

This audit does not cover generating an address (the address-generation family).

This audit does not cover reading an address out of a document (the address-extraction family).

This audit does not cover confirming receipt of a payment (the payment-receipt family).

This audit does not cover reading a spreadsheet (the spreadsheet-reading family).

This audit does not cover generating a spreadsheet (the spreadsheet-generation family).

This audit does not cover reading a Word document (the Word-reading family).

This audit does not cover generating a Word document (the Word-generation family).

This audit does not cover reading a presentation (the presentation-reading family).

This audit does not cover generating a presentation (the presentation-generation family).

This audit does not cover extracting text from a PDF (the PDF-extraction family).

This audit does not cover generating a PDF (the PDF-generation family).

This audit does not cover merging PDFs (the PDF-merging family).

This audit does not cover splitting a PDF (the PDF-splitting family).

This audit does not cover rotating a PDF (the PDF-rotation family).

This audit does not cover filling a PDF form (the PDF-form-filling family).

This audit does not cover watermarking a PDF (the PDF-watermarking family).

This audit does not cover redacting a PDF (the PDF-redaction family).

This audit does not cover compressing a PDF (the PDF-compression family).

This audit does not cover annotating a PDF (the PDF-annotation family).

This audit does not cover extracting a table (the table-extraction family).

This audit does not cover reading text from an image (the OCR family).

This audit does not cover extracting data from a document (the document-data-extraction family).

This audit does not cover signing a document electronically (the e-signature family).

This audit does not cover recording a screen (the screen-recording family).

This audit does not cover generating a video (the video-generation family).

This audit does not cover generating a QR code (the QR-generation family).

This audit does not cover generating a barcode (the barcode-generation family).

This audit does not cover scanning a barcode (the barcode-scanning family).

This audit does not cover mixing audio (the audio-mixing family).

This audit does not cover generating audio (the audio-generation family).

This audit does not cover editing audio (the audio-editing family).

This audit does not cover separating audio sources (the audio-source-separation family).

This audit does not cover recognising speech (the speech-recognition family).

This audit does not cover synthesising speech (the speech-synthesis family).

This audit does not cover reducing noise (the noise-reduction family).

This audit does not cover generating music (the music-generation family).

This audit does not cover transcribing music (the music-transcription family).

This audit does not cover checking whether a chemical identifier string is well-formed (the InChI family).

This audit does not cover checking whether a chemical notation string is well-formed (the SMILES family).

This audit does not cover checking whether a European Community number string is well-formed (the EC-number family).

This audit does not cover checking whether a United Nations transport number string is well-formed (the UN-transport-number family).

This audit does not cover looking up a compound in PubChem (the PubChem-query family).

This audit does not cover checking whether a chemical structure is well-formed (the chemical-structure-validation family).

This audit does not cover checking whether any other chemical identifier string is well-formed (the other-chemical-identifiers family).

This audit does not cover reading a container number out of a shipping document (the container-number-reading family).

This audit does not cover looking up a carrier registration by container number (the carrier-registry family).

This audit does not cover checking whether a shipowner code is registered (the BIC-shipowner-code family).

This audit does not cover checking whether a container size-type code is well-formed (the container-size-type family).

This audit does not cover generating a new container number (the container-number-generation family).

This audit does not cover checking whether a container number string is well-formed (the ISO-6346-validation family).

This audit does not cover fetching a library's record from a registry over the network (the library-record-fetching family).

This audit does not cover registering a new library identifier with an agency (the library-identifier-registration family).

This audit does not cover cataloguing a library collection or reading a MARC record (the cataloguing family).

This audit does not cover looking a library up in OCLC or WorldCat (the OCLC-WorldCat family).

This audit does not cover listing the agencies that issue library identifiers (the library-agency-listing family).

This audit does not cover checking whether a library-identifier string is well-formed (the ISIL-validation family).

This audit does not cover checking whether a ship-number string is well-formed (the IMO-validation family).

This audit does not cover checking whether a maritime mobile identity string is well-formed (the MMSI-validation family).

This audit does not cover checking whether a hull identification number string is well-formed (the HIN-validation family).

This audit does not cover checking whether a European vessel number string is well-formed (the ENI-validation family).

This audit does not cover looking a vessel up in a ship registry (the vessel-registry-lookup family).

This audit does not cover tracking a vessel by AIS (the AIS-tracking family).

This audit does not cover looking a ship up by name (the ship-name-lookup family).

This audit does not cover checking whether a subscriber-identity string is well-formed (the IMSI-validation family).

This audit does not cover looking a tax identifier up in the EU VIES registry over the network (the VIES-lookup family — a registry query, not a string judgement).

This audit does not cover looking up the tax rate for a country (the VAT-rate-lookup family).

This audit does not cover computing tax amounts on an invoice (the tax-calculation family).

This audit does not cover generating an invoice document (the invoice-generation family).

This audit does not cover checking whether a tax-identifier string is well-formed (the VATIN-validation family — a VATIN is a country code plus a country-specific identifier, and judging one says nothing about a DOI).

This audit does not cover checking whether a SEPA structured creditor reference string is well-formed (the SEPA-creditor-reference family — an RF reference judged by the ISO 11649 check, a different identifier from a DOI).

This audit does not cover reading an unstructured invoice or payment reference out of a document (the invoice-reference-extraction family).

This audit does not cover looking a payment up by its creditor reference (the payment-lookup family — a registry query, not a string judgement).

This audit does not cover generating a new creditor reference (the creditor-reference-generation family — minting a fresh string never judges an existing one).

This audit does not cover checking whether a classification code string is well-formed (the financial-instrument-classification family — a six-letter ISO 10962 code judged by a classification table, and judging one says nothing about a DOI).

