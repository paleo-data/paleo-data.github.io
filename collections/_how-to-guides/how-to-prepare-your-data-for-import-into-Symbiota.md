---
title: Prepare your data for import into Symbiota
last_modified_at: 2025-04-23
sidebar:
  nav: [sidebar]
toc: True
toc_sticky: True
sidebar:
  nav:
  - sidebar
  collapsible: true
  expanded:
  - how-to-guides
topics: [symbiota, data wrangling]
---

{: .notice--info }
This guide is intended to complement documentation for [getting started in the Symbiota Paleo Data Portal](/knowledge-hub/how-to-guides/how-to-get-started-in-the-symbiota-paleo-data-portal.html), as well as the official Symbiota user documentation, [_Symbiota Docs_](https://biokic.github.io/symbiota-docs/). _Symbiota Docs_ provides general guidance for working in Symbiota-based data portals and should be referenced for basic functions and workflows. This manual expands on this resource to provide discipline-specific information for fossil collections.

This document outlines actions you can take to prepare existing digital catalog records from your fossil collection for ingestion into Symbiota. These steps can help make your data more easily managed and discovered, and are therefore _highly_ recommended.

## Formatting data for import

### Steps you can take to ready your records for ingestion
1. Familiarize yourself with the [Darwin Core data standard](https://dwc.tdwg.org/terms/), which is the basis for the majority of [Symbiota’s Data Fields](https://biokic.github.io/symbiota-docs/editor/edit/fields/).
2. If you maintain existing catalog records to be imported into Symbiota, perform some data cleaning to align your records to the Symbiota data fields and formatting specified in the previous step. [OpenRefine](https://doi.org/10.5281/zenodo.6574728) is free software that can be used for this purpose. **Highly recommended: Use the checklist below to prepare your data for import.**
3. If you’d like a template to follow, [this spreadsheet](https://docs.google.com/spreadsheets/d/1b1aN6NuoOEN4IlToV3Uk33xpSwrbcn3-uceSnlgf8JI/edit?usp=sharing) is preformatted for use with Symbiota. Not all fields are required to contain data. Your spreadsheet must be converted to CSV format prior to ingestion into the portal, which can be easily accomplished in a program like [Microsoft Excel](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) or [Google Sheets](https://support.google.com/docs/answer/49114?sjid=17532513690429081890-NC).

#### Data formatting checklist
If you maintain cataloged specimen records in a spreadsheet, this information can be imported into Symbiota in CSV format. Before doing so, it is highly recommended that you use this checklist to prepare your data for ingestion to maximize the interoperability between your data and that of other collections, ultimately making your records more discoverable and useful for research. Additional data cleaning can be performed once your records are in Symbiota. The checklist below has been compiled based on scenarios observed in other datasets from fossil collections prepared for import. The [Symbiota Data Import Fields](https://biokic.github.io/symbiota-docs/coll_manager/upload/fields/) guide provides important information about fields available in Symbiota, as well as the types of data that can be imported into each one—for instance, which fields can only contain numbers, dates only, textual data, etc.—and how this information should be formatted. ~Examples of datasets that have been cleaned in preparation for ingestion into Symbiota can be found [here]()~. 

| Dataset | After Cleaning |
| --------------- | ------ |
| ASU Paleobotany | [link] | 
| PH Paleobotany  | [link] |

- [ ] Catalog Numbers: Every occurrence (=specimen record) to be imported must have a catalog number assigned. Example: “USNM000001”.
- [x] Catalog Numbers: Every occurrence (=specimen record) to be imported must have a catalog number assigned. Example: “USNM000001”.
      
| Checklist Item | Recommendation | Example |
| -------------- | -------------- | ------- |
| **Catalog Numbers** | Every occurrence (=specimen record) to be imported must have a catalog number assigned. | `USNM000001` |
| **Secondary identifiers** | [Parse](https://biokic.github.io/symbiota-docs/editor/edit/fields/catno/) into a semicolon delimited list of `key:value` pairs (i.e., tagName: identifier). | _otherCatalogNumbers_ = `legacy catalog number: ASU 3541; accession number: WIS-L-001456` |
| **Delimiters** | Use pipes (`|`) or semicolons to separate values in a list, and be consistent with formatting. Doing so will facilitate parsing of data, if ever needed, in the future. Avoid using [commas](https://www.hbs.edu/research-computing-services/data-practices/database-best-practices/delimiters.aspx#:~:text=Word%20of%20Caution%20on%20Delimiters&text=Often%2C%20the%20comma%20is%20used,4%20fields%20instead%20of%203!&text=When%20exporting%20data%2C%20you%20should,also%20occur%20within%20your%20data.) as delimiters. | _Associated Collectors_ = `Charlotte Hill | Samuel Scudder | Arthur Lakes` |
| **Fields containing different kinds of information** | When this is unavoidable, use `key:value` pairs to concatenate data that must be combined into one field. | _Occurrence Remarks_ = `ACQUISITION DETAILS: Gift of Arthur Lakes April 1890 | NOTES: Original specimen label misplaced`. |
| **Dates** | Fields containing dates should be formatted in [ISO format](https://www.iso.org/iso-8601-date-and-time-format.html), e.g. YYYY-MM-DD. An exception to this rule is [_verbatimEventDate_](https://dwc.tdwg.org/terms/#dwc:verbatimEventDate); use this field when dates are incomplete or not ISO formatted. | `1998-11-30` |
| **Identifications** | For specimens identified above the species level, do not include `sp.`, `indet.`, or similar suffixes. Qualifiers like `aff.` and `?` should be recorded in a separate field, [_identificationQualifier_](https://dwc.tdwg.org/terms/#dwc:identificationQualifier). Verbatim label identifications (e.g. `Lepidophyllum [?]` can be captured in [_identificationRemarks_](https://dwc.tdwg.org/terms/#dwc:identificationRemarks). Leave blank for specimens/specimen lots without identifications. Refer to Symbiota-specific guidance for [_scientificName_ vs. _sciName_](https://biokic.github.io/symbiota-docs/coll_manager/upload/fields/). | _scientificName_=`Phylledestes vorax Cockerell, 1907` or _sciName_=`Phylledestes vorax` |
| **Localities** | If any locality data should be [obscured](https://biokic.github.io/symbiota-docs/coll_manager/data_publishing/redaction/), include a _locationSecurity_ column in your spreadsheet and give records with sensitive locality data a value of “1”. | |
| **Geological time** | Conform values to the [ICS Time Scale](https://stratigraphy.org/chart) and use “Early” in place of “Upper” and “Late” in place of “Lower”. Provide values for both _earlyInterval_ and _lateInterval_, even if both values are the same. | _earlyInterval_ = `Late Jurassic` and _lateInterval_ = `Early Cretaceous` |
| **Geological units** | Values for _group_, _formation_, _member_, and _bed_ should be parsed into [the appropriate fields](https://dwc.tdwg.org/terms/#dwc:formation). | _formation_ = `Wasatch Formation` and _member_ = `Niland Tongue` |
| **Vocabularies** | If your dataset contains anatomical elements that may benefit from the use of a controlled vocabulary, refer to these [examples](https://drive.google.com/drive/folders/1aNHpsLJLuVOubVmbohOZk2VbfDv3BlLH?usp=drive_link). | |
| **Type specimens** | Include a value in [_typeStatus_](https://dwc.tdwg.org/terms/#dwc:typeStatus) ([ICZN](https://www.iczn.org/outreach/faqs/#faq-4) and [IAPT](https://www.iapt-taxon.org/nomen/pages/main/art_9.html) values preferred). [See below]() for information about “extending” your specimens that are referenced in literature. | `syntype` |
| **File format** | Save your spreadsheet in comma-separated (CSV) format. Additionally, to ensure any special or accented characters import correctly, always save your data import files using [UTF-8](https://www.w3schools.com/charsets/ref_html_utf8.asp) character encoding. | |
| **Cataloging specimen lots** | When multiple individuals of a single taxon exist in a given lot (i.e. isolated in one physical container), they can be cataloged as a single occurrence record. [See below]() for advice when a lot contains multiple taxa. | |
| **Cataloging part-counterpart pairs and similar relationships between records** | [See below]() for information about “extending” your specimens. | |

{% include resource_card filename='pearson-2022.yml' %}

{% include related_list topics='symbiota' %}

{% include resource_list topics='symbiota' %}
