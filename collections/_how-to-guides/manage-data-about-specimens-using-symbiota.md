---
title: Manage data about fossil specimens using Symbiota
topics: [symbiota, extended specimen, manage data]
sidebar:
  nav: [sidebar]
  collapsible: true
  expanded: [how-to-guides]
toc: true
toc_sticky: true
status: published
contributors: ["Lindsay Walker"]
last_modified_at: 2025-07-31
---

{: .notice--primary }
This guide is intended to complement documentation for [getting started in the Symbiota Paleo Data Portal](/knowledge-hub/how-to-guides/start-using-symbiota), as well as the official Symbiota user documentation, [Symbiota Docs](https://docs.symbiota.org/about). Symbiota Docs provides general guidance for working in Symbiota-based data portals and should be referenced for basic functions and workflows. This manual expands on this resource to provide discipline-specific information for fossil collections.

# Introduction
There are two ways specimen records are typically entered into a Symbiota portal: 1) as a [bulk data import](#bulk-data-import) or 2) [directly using the Occurrence Editor interface](#direct-data-entry). Additional methods exist, but these are the most commonly used options by collections that actively ("live") manage their specimen data using Symbiota. In all cases, the end goal is to make your data more easily managed, discovered, and used for research; thus, data providers are strongly encourged to follow the steps outlined in this how-to guide.

Regardless of data entry method, it is important that all data providers become familiar with the [Darwin Core data standard](https://dwc.tdwg.org/terms/), which forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields).

{: .notice--success }
[Exemplar catalog records](https://paleo.symbiota.org/portal/collections/list.php?db=6) are in the process of being created as a reference to guide data entry for fossil specimens in Symbiota portals. It may be helpful to bookmark this page for ease of access.

# Bulk data import
## Formatting data for import
This section outlines actions you can take to prepare and import existing digital catalog records from your fossil collection into a Symbiota portal.

### Steps you can take to ready your records for ingestion
1. If you maintain existing catalog records to be imported into Symbiota, perform some data cleaning to align your records to Symbiota's data fields and formatting requirements. The [data formatting checklist](#data-formatting-checklist) is intended to inform this process, and [OpenRefine](https://openrefine.org) is free software that can be used for this purpose. Additional data cleaning can be performed once your records have been imported into Symbiota. 
2. If you’d like a template to follow, [this spreadsheet](https://docs.google.com/spreadsheets/d/1b1aN6NuoOEN4IlToV3Uk33xpSwrbcn3-uceSnlgf8JI/edit?usp=sharing) is preformatted for use with Symbiota. Your spreadsheet must be converted to CSV format (use UTF-8 character encoding) prior to ingestion into the portal, which can be easily accomplished in a program like [Microsoft Excel](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) or [Google Sheets](https://support.google.com/docs/answer/49114?sjid=17532513690429081890-NC). An expanded version of this spreadsheet can be provided [upon request](mailto:paleoinformatics@gmail.com).

{% include resource_card filename='krimmel-walker-2022.yml' %}

## How to import your data into Symbiota
There are multiple ways to import new records into a Symbiota portal. This action can only be completed by users with Administrator permissions through the Administration Control Panel.
- To import a spreadsheet of specimen occurrence data, use the “[Full Text File Import](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/)” option.
- To import a spreadsheet of extended specimen data, use the “[Extended Data Import](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources)” option. [See below](#extending-your-specimens) for more information about how to extend your specimens using Symbiota.

{: .notice--danger }
**Recommendation:** Import one or a very small number of representative records prior to initiating a larger import, especially if you are new to this process. Doing so will allow you to assess how your records will look in the portal. Similar to bulk data ingestion, only users with Administrator permissions can delete records, and this action cannot be done in bulk; records can only be deleted one-by-one using the Admin tab interface on the Occurrence Editor.

## Steps you can take immediately after your records are in Symbiota
- Moving forward, make edits to your records and complete other management tasks, like managing loans, directly in Symbiota.
- Save your import spreadsheets somewhere safe, but you likely will not need them again once the records are ingested into your Symbiota portal.
- Run your portal's [built-in data cleaning tools](https://docs.symbiota.org/Collection_Manager_Guide/Data_Cleaning/) to ingest new taxonomy and clean geographic location details.
- Further clean your data using tips in the [Symbiota Data Quality Toolkit](https://docs.symbiota.org/Editor_Guide/data_quality_toolkit).
- [Georeference](https://tdwg.github.io/esp/georeferencing/workflows.html) your specimen records.

{: .notice--primary }
💡 The last two steps can be delegated to users with Editor permissions, such as students or volunteers!

# Direct data entry
The content in this section outlines recommendations for direct data entry using Symbiota's Occurrence Editor interface, which allows users with Administrator and Editor user permissions to add and edit specimen records in Symbiota. As a reminder, the [Darwin Core data standard](https://dwc.tdwg.org/terms/) forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields). This guide is intentionally designed help make your data more easily managed, discovered, and used for research; data providers are thus strongly encourged to conform with the recommendations outlined in this section.

<iframe src="https://docs.google.com/presentation/d/1yJFsaCnBC28zW8UtLfl3tnJayk3w-BRDtVzyZYpD1TI/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

# How do I keep my records clean once they’re available in Symbiota?
## Prevent new errors
When training new staff or volunteers on data entry or management, it is **highly** recommended that you point them toward this Knowledge Hub, but more specifically, have them become familiar with the [Symbiota Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) and the [data formatting checklist](#data-formatting-checklist).

## Mitigate existing errors
Mistakes are likely to happen, even in carefully curated datasets. It is therefore recommended that you routinely assess your data using the [Symbiota Data Quality Toolkit](https://biokic.github.io/symbiota-docs/editor/quality/). This guide is designed to enable users with either Administrator or Editor permissions to your Collection Profile to “clean” your data–i.e. find and correct errors–using the portal’s built-in features wherever possible.

## Crowdsource quality control
Symbiota maintains several built-in tools to facilitate collaborative data entry and data cleaning when enabled for your collection.  For example, Administrators of a given collection can enable any portal user who is logged in with an account to suggest edits to your records in the portal. Suggestions must be reviewed by an Administrator before they become public. By default, this option is turned **off**, but it can be activated through your Administrator Control Panel. Review [Symbiota Docs](https://docs.symbiota.org/Collection_Manager_Guide/Comments_Feedback/public_edits/) for more information about this feature. 

## Set up a data import profile
If you intend to repeatidly import data using a standard import template--for example, if you intend to cataloging using a spreadsheet method--you can set up a new data [import profile](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/#initiating-the-upload) based on your cleaned spreadsheet.

# Appendices

## Data formatting checklist
Before importing existing catalog records into Symbiota, complete this checklist to prepare your data for ingestion. **The aim is to maximize interoperability between records in your dataset and other fossil collections, ultimately making your data more discoverable and useful for research**. The checklist below has been compiled based on commonly encountered scenarios in fossil collections; however, it is not comprehensive and should only serve as a starting point.

{: .notice--success }
When preparing your data, refer to [Symbiota’s Data Import Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) for field definitions, as well as [this page](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/data_import_fields) to learn what types of data can be imported, e.g., which fields can only contain numbers, dates, textual data, etc.
 
| Checklist Item | Recommendation |
| - | - |
| **Catalog Numbers** | Every occurrence (catalog record) to be imported must have a unique catalog number. <br>**Example:** `USNMV18414` |
| **Basis of Record** | Every record corresponding to cataloged fossil material should receive the [_basisOfRecord_](https://dwc.tdwg.org/terms/#dwc:basisofrecord) value, "FossilSpecimen". <br>**Example:** _basisOfRecord_ = `FossilSpecimen` |
| **Secondary identifiers** | Parse [secondary identifiers](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/catalog_numbers#tag-name--additional-identifier-values--other-catalog-numbers) into a semicolon-delimited list of `key: value` pairs (i.e., tagName: identifier). <br>**Example:** _otherCatalogNumbers_ = `Old Catalog Number: ASU 3541; Accession Number: WIS-L-001456` |
| **Delimiters** | Use pipes (`|`) or semicolons to separate values in lists and be consistent with formatting. Doing so will facilitate parsing of data, if ever needed, in the future. Avoid using [commas](https://www.hbs.edu/research-computing-services/data-practices/database-best-practices/delimiters.aspx#:~:text=Word%20of%20Caution%20on%20Delimiters&text=Often%2C%20the%20comma%20is%20used,4%20fields%20instead%20of%203!&text=When%20exporting%20data%2C%20you%20should,also%20occur%20within%20your%20data.) as delimiters. <br>**Example:** _Element_ = `stem | strobilus | root` |
| **Dates** | Fields containing dates should be formatted in [ISO format](https://www.iso.org/iso-8601-date-and-time-format.html), e.g. YYYY-MM-DD. An exception to this rule is [_verbatimEventDate_](https://dwc.tdwg.org/terms/#dwc:verbatimEventDate); use this field when dates are incomplete or not ISO formatted. |
| **Identifications** | For specimens identified above the species level, do not include `sp.`, `indet.`, or similar suffixes. Qualifiers like `aff.` and `?` should be recorded in a separate field, [_identificationQualifier_](https://dwc.tdwg.org/terms/#dwc:identificationQualifier). Verbatim label identifications (e.g. `Lepidophyllum [?]` can be captured in [_identificationRemarks_](https://dwc.tdwg.org/terms/#dwc:identificationRemarks). Leave blank for specimens/specimen lots without identifications. Refer to Symbiota-specific guidance for [_scientificName_ vs. _sciName_](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/data_import_fields). <br>**Example:** _scientificName_=`Phylledestes vorax Cockerell, 1907` or _sciName_=`Phylledestes vorax` |
| **Localities** | If any locality data should be [obscured](https://docs.symbiota.org/Collection_Manager_Guide/Data_Publishing/redacting_obscuring_data/), include a _locationSecurity_ column in your spreadsheet and give records with sensitive locality data a value of “1”. |
| **Geological time** | Refer to Symbiota Docs for important [data field definitions](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#paleontology-fields) and [related instructions](https://docs.symbiota.org/Collection_Manager_Guide/paleo_data). See important notice below regarding **verbatim values in geological context data**.<br>**Example:** _earlyInterval_ = `Late Jurassic` and _lateInterval_ = `Early Cretaceous` |
| **Geological units** | Refer to Symbiota Docs for important [data field definitions](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#paleontology-fields) and see notice below regarding **verbatim values in geological context data**.<br>**Example:** _formation_ = `Wasatch` and _member_ = `Niland Tongue` |
| **Contextual descriptions** | Refer to the field definitions for [_Description_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#description), [_Element_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#element), and [_Individual Count_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#individual-count) for important information about how to format data related to anatomy and the physical nature of cataloged fossil matieral. **Example:** see demo record for [USNMPAL144776](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763845) |
| **Vocabularies** | If your dataset contains anatomical elements that may benefit from the use of a controlled vocabulary, refer to these [examples](https://drive.google.com/drive/folders/1aNHpsLJLuVOubVmbohOZk2VbfDv3BlLH?usp=drive_link). |
| **Cataloging multi-specimen lots** | When multiple individuals of a single taxon exist in a given lot (i.e. isolated in one physical container), they can be cataloged as a single occurrence record. [See below](#cataloging-multi-taxon-specimen-lots) for advice when a lot contains multiple taxa. |
| **Fields containing different kinds of information** | When this is unavoidable, use `key:value` pairs to concatenate data that must be combined into one field. <br>**Example:** _Occurrence Remarks_ = `ACQUISITION DETAILS: Gift of Arthur Lakes April 1890 | NOTES: Original specimen label misplaced`. |
| **Type specimens** | Include a value in [_typeStatus_](https://dwc.tdwg.org/terms/#dwc:typeStatus) ([ICZN](https://www.iczn.org/outreach/faqs/#faq-4) and [IAPT](https://www.iapt-taxon.org/nomen/pages/main/art_9.html) values preferred). [See below](#type-and-referred-specimens) for information about “extending” your specimens that are referenced in literature. |
| **File format** | Save your finalized spreadsheet in comma-separated (CSV) format. Additionally, to ensure any special or accented characters import correctly, always save your data import files using [UTF-8](https://www.w3schools.com/charsets/ref_html_utf8.asp) character encoding. |

{: .notice--warning }
**A note on verbatim values in geological context data:** Many fossil specimens are accompanied by labels, field notes, and other primary data sources containing values that are no longer accepted (e.g. "Tertiary"), informally used (e.g. "Precambrian"), or indicate uncertainty (e.g., "Upper Mio?"). This information is important and should be recorded; however, it should not be captured using Symbiota's _earlyInterval_ and _lateInterval_ fields, which map to a portal's standardized geological time scale values (by default, these values are based on the [ICS Time Scale](https://stratigraphy.org/chart)). In the absence of an appropriate, standard-based term to record these data, this information should be captured in _stratigraphicRemarks_ as a key:value pair.<br> **[Example](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763806):** `VERBATIM CHRONOSTRATIGRAPHY: Permian?`

{: .notice--warning }
**A note on commonly encountered scenarios:** Suggested solutions to several commonly encountered cataloging scenarios--such as dealing with "part-counterpart" specimens and similar scenarios--are further detailed [below](#part-counterpart-specimens-and-similar-scenarios).

## Extending your specimens
Once your occurrence records are available in Symbiota, associations can be created between your specimen data in Symbiota and external resources, including digitally available literature and other occurrence records (both in and external to your Symbiota portal). This can be accomplished using two methods. Users with Editor or Administrator permissions can create these linkages one-by-one using the [Linked Resources tab](https://docs.symbiota.org/Editor_Guide/linking_records); additionally, users with Administrator permissions can create these linkages in batch by uploading a CSV-formatted spreadsheet using the [Extended Data Import tool](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources). The latter option contains several fields that are not available in the Linked Resources tab, such as _accordingTo_.

{: .notice--warning }
**Tip:** When creating associations with external resources, provide a **stable URL**—like a DOI or a permalink—for the _resourceURL_ whenever possible.

{: .notice--primary }
Examples of "Extended Specimens" in Symbiota are available in [this dataset] [URL forthcoming].

### Type and referred specimens
You can create linkages between occurrence records in your Symbiota portal and digitally available publications using the fields and parameters specified below.

**Examples:** 1) [USNMV4735](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763793) (holotype of _Ceratosaurus nasicornis_); 2) [USNM P34765](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763783) (specimen of _Carya libbeyii_ that has been referenced in several publications) 
- _Association Type_ = `Non-occurrence Resource`
- _Relationship Type_ = `isReferencedBy`

| subjectCatalogNumber | basisOfRecord | accordingTo | resourceURL |
| - | - | - | - |
| USNMP34765 | ReferenceCitation | Knowlton; 1916; Proceedings of the National Museum | [https://www.biodiversitylibrary.org/page/7764079](https://www.biodiversitylibrary.org/page/7764079) |
| USNMV4735 | ReferenceCitation | Carrano & Choinier; 2016; Journal of Vertebrate Paleontology | [https://doi.org/10.1080/02724634.2015.1054497](https://doi.org/10.1080/02724634.2015.1054497) |

### Part-counterpart specimens and similar scenarios
#### Scenario A: One institution owns all pieces of a fossil specimen
You can create associations between one or more occurrence records cataloged in your Symbiota portal using the fields and parameters specified below.

**Example:** [ANSP3472](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763807) (part) and [ANSP3473](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763808) (counterpart) were cataloged as separate records within the same Symbiota portal and subsequently linked as associated records.
- _Association Type_ = `Occurrence - Internal (this portal)`
- _Relationship Type_ = `part` OR `counterpart` (describe the specimen being linked to)

| subjectCatalogNumber | objectCatalogNumber | basisOfRecord |
| - | - | - |
| ANSP3472 | ANSP4373 | FossilSpecimen |

{: .notice--primary }
Think of the “**subject**” as the “**part**” and the “**object**” as the “**counterpart**” when creating a a part-counterpart pairing in Symbiota. Both records must already exist in the portal in order to create this type of relationship.

{: .notice--primary }
**Alternative method:** If you prefer to catalog part-counterpart specimens as a single specimen record, this is also possible, as in this [example]().

#### Scenario B: Multiple institutions own different pieces of a fossil specimen
Similarly, associations can be created between specimen occurrences in your Symbiota portal and occurrences in other data portals—**for example, if your collection maintains one half of a part-counterpart pair, one or more pieces of an individual cataloged by different institutions, or a specimen-cast pairing.** In all of these cases, you can create linkages between your catalog records in Symbiota and records hosted in external portals.

**Example:** [USNM PAL 603860](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763802) (cataloged in Symbiota) is a cast of [YPM VP 058990](https://collections.peabody.yale.edu/search/Record/YPM-VP-058990) (cataloged in an external database). An association has been created between these records in Symbiota.
- _Association Type_ = `Occurrence - External Link`
- _Relationship Type_ = value varies depending on the association to be created

| subjectCatalogNumber | objectID | basisOfRecord | verbatimSciname | resourceURL |
| - | - | - | - | - |
| USNMPAL603860 | YPMVP058990 | FossilSpecimen | Goleroconus alfi | [https://collections.peabody.yale.edu/search/Record/YPM-VP-058990](https://collections.peabody.yale.edu/search/Record/YPM-VP-058990) |

{: .notice--primary }
Think of the “**subject**” as the piece of specimen retained in your collection (cataloged in Symbiota) and the “**object**” as part retained in an external collection. The _verbatimSciName_ refers to the identification of the occurrence maintained by the external collection.

### Cataloging multi-taxon specimen lots
_Content forthcoming_

{: .notice--primary }
📬 **Questions?** Data providers are encouraged to contact [paleoinformatics@gmail.com](mailto:paleoinformatics@gmail.com) for assistance with questions related to importing and maintaining fossil specimen data using Symbiota. Include “Symbiota” in the subject of your email, e.g. “Help with preparing my data for the Symbiota Paleo Data Portal”. 
