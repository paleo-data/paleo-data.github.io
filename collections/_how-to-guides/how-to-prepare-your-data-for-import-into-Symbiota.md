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
      
| Checklist Item | Recommendation |
| -------------- | -------------- |
| **Catalog Numbers** | Every occurrence (=specimen record) to be imported must have a catalog number assigned. Example: `USNM000001`. |
|`**Secondary identifiers** | [Parse](https://biokic.github.io/symbiota-docs/editor/edit/fields/catno/) into a semicolon delimited list of key:value pairs (i.e., tagName: identifier). Example: _otherCatalogNumbers_ = `legacy catalog number: ASU 3541; accession number: WIS-L-001456`. |
| **Delimiters** | Use pipes (`|`) or semicolons to separate values in a list, and be consistent with formatting. Doing so will facilitate parsing of data, if ever needed, in the future. Avoid using [commas]() as delimiters. Example: _Associated Collectors_ = `Charlotte Hill | Samuel Scudder | Arthur Lakes` |
| **Fields containing different kinds of information** | When this is unavoidable, use `key:value` pairs to concatenate data that must be combined into one field. Example: _Occurrence Remarks_ = `ACQUISITION DETAILS: Gift of Arthur Lakes April 1890 | NOTES: Original specimen label misplaced`.

{% include resource_card filename='pearson-2022.yml' %}

{% include related_list topics='symbiota' %}

{% include resource_list topics='symbiota' %}
