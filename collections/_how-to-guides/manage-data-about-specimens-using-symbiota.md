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
last_modified_at: 2025-08-17
---

{: .notice--primary }
This guide is intended to complement documentation for [getting started in the Symbiota Paleo Data Portal](/knowledge-hub/how-to-guides/start-using-symbiota), as well as the official Symbiota user documentation, [Symbiota Docs](https://docs.symbiota.org/about). Symbiota Docs provides general guidance for working in Symbiota-based data portals and should be referenced for basic functions and workflows. This manual expands on this resource to provide discipline-specific information for fossil collections.

## Introduction
There are two ways specimen records are typically entered into a Symbiota portal: 1) as a [bulk data import](#bulk-data-import) or 2) [directly using the Occurrence Editor interface](#direct-data-entry). Additional methods exist, but these are the most commonly used options by collections that actively ("live") manage their specimen data using Symbiota. In all cases, the end goal is to make your data more easily managed, discovered, and used for research; thus, data providers are strongly encourged to follow the steps outlined in this how-to guide.

Regardless of data entry method, it is important that all data providers become familiar with the [Darwin Core data standard](https://dwc.tdwg.org/terms/), which forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields).

{: .notice--success }
[Exemplar catalog records](https://paleo.symbiota.org/portal/collections/list.php?db=6) are in the process of being created as a reference to guide data entry for fossil specimens in Symbiota portals. It may be helpful to bookmark this page for ease of access.

## Bulk data import
### Formatting data for import
This section outlines actions you can take to prepare and import (ingest) existing digital catalog records from your fossil collection into a Symbiota portal.

**I. Prepare your records for import:** <br>
- If you maintain existing catalog records to be imported into Symbiota, perform some data cleaning to align your records to Symbiota's data fields and formatting requirements. The [data formatting checklist](#data-formatting-checklist) is intended to inform this process, and [OpenRefine](https://openrefine.org) is free software that can be used for this purpose. Additional data cleaning can be performed once your records have been imported into Symbiota.
- If you’d like a template to follow, [this spreadsheet](https://docs.google.com/spreadsheets/d/1b1aN6NuoOEN4IlToV3Uk33xpSwrbcn3-uceSnlgf8JI/edit?usp=sharing) is preformatted for use with Symbiota. Your spreadsheet must be converted to CSV format (use UTF-8 character encoding) prior to ingestion into the portal, which can be easily accomplished in a program like [Microsoft Excel](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) or [Google Sheets](https://support.google.com/docs/answer/49114?sjid=17532513690429081890-NC). An expanded version of this spreadsheet can be provided [upon request](mailto:paleoinformatics@gmail.com).

{% include resource_card filename='krimmel-walker-2022.yml' %}

**2. Import your data into Symbiota:** <br>
There are multiple ways to import new records into a Symbiota portal. This action can only be completed by users with Administrator permissions through the Administration Control Panel.
- To import a spreadsheet of specimen occurrence data, use the “[Full Text File Import](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/)” option.
- To import a spreadsheet of extended specimen data, use the “[Extended Data Import](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources)” option. [See below](#extending-your-specimens) for more information about how to extend your specimens using Symbiota.

{: .notice--danger }
Import one or a very small number of representative records prior to initiating a larger import, especially if you are new to this process. Doing so will allow you to assess how your records will look in the portal. Similar to bulk data ingestion, only users with Administrator permissions can delete records, and this action cannot be done in bulk; records can only be deleted one-by-one using the Admin tab interface on the Occurrence Editor.

**3. Once your records are in Symbiota:** <br>
- Moving forward, make edits to your records and complete other management tasks, like managing loans, directly in Symbiota.
- Save your import spreadsheets somewhere safe, but you likely will not need them again once the records are ingested into your Symbiota portal.
- Run your portal's [built-in data cleaning tools](https://docs.symbiota.org/Collection_Manager_Guide/Data_Cleaning/) to ingest new taxonomy and clean geographic location details.
- Further clean your data using tips in the [Symbiota Data Quality Toolkit](https://docs.symbiota.org/Editor_Guide/data_quality_toolkit).
- [Georeference](https://tdwg.github.io/esp/georeferencing/workflows.html) your specimen records.

{: .notice--success }
The last two steps can be delegated to users with Editor permissions, such as students or volunteers!

## Direct data entry
The content in this section outlines recommendations for direct data entry using Symbiota's Occurrence Editor interface, which allows users with Administrator and Editor user permissions to add and edit specimen records in Symbiota. As a reminder, the [Darwin Core data standard](https://dwc.tdwg.org/terms/) forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields). This guide is intentionally designed help make your data more easily managed, discovered, and used for research; data providers are thus strongly encourged to conform with the recommendations outlined in this section.

<iframe src="https://docs.google.com/presentation/d/1yJFsaCnBC28zW8UtLfl3tnJayk3w-BRDtVzyZYpD1TI/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Data quality maintenance
Once your records are imported or entered directly into Symbiota, some effort will be required to correct, maintain, or improve the quality of your specimen data. These activities will be ongoing, and the following recommendations are made to help you begin this process.

**Prevent new errors** <br>
When training new staff or volunteers on data entry or management, it is **highly** recommended that you point them toward this Knowledge Hub, but more specifically, have them become familiar with the [Symbiota Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) and the [data formatting checklist](#data-formatting-checklist).

**Mitigate existing errors** <br>
Mistakes are likely to happen, even in carefully curated datasets. It is therefore recommended that you routinely assess your data using the [Symbiota Data Quality Toolkit](https://biokic.github.io/symbiota-docs/editor/quality/). This guide is designed to enable users with either Administrator or Editor permissions to your Collection Profile to “clean” your data–i.e. find and correct errors–using the portal’s built-in features wherever possible.

**Crowdsource quality control** <br>
Symbiota maintains several built-in tools to facilitate collaborative data entry and data cleaning when enabled for your collection.  For example, Administrators of a given collection can enable any portal user who is logged in with an account to suggest edits to your records in the portal. Suggestions must be reviewed by an Administrator before they become public. By default, this option is turned **off**, but it can be activated through your Administrator Control Panel. Review [Symbiota Docs](https://docs.symbiota.org/Collection_Manager_Guide/Comments_Feedback/public_edits/) for more information about this feature. 

**Set up a data import profile** <br>
If you intend to routinely import data using a standard import template--for example, if you intend to cataloging using a spreadsheet method--you can set up a new data [import profile](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/#initiating-the-upload) based on your cleaned spreadsheet.

## Appendices

### Cataloging scenarios unique to fossils

#### Part-counterpart specimens
"Part" and "counterpart" specimens refer to fossils that have been physically separated, such that the individual organism(s) originally contained in one piece of rock now exist in multiple pieces. For example, [split shale](https://www.gbif.org/occurrence/1950905513) and [broken concretions](https://www.gbif.org/occurrence/4029672311) commonly result in part-counterpart specimens.

##### Recommended method
Guidance regarding newly curated part-counterpart specimens is actively in development by [PDWG](https://paleo-data.github.io/knowledge-hub/community/about-pdwg). Until this information is formalized, the following method is recommended for treating these specimens using Symbiota. This guidance is expected to evolve.

* Create one catalog record corresponding to all pieces of a part-counterpart specimen. Doing so will avoid confusion for downstream data users, as creating multiple records for one biological individual is not advised at this time.
* Include all data available, per usual (collector info, locality, geological context, etc.).
* Additionally, the record should include:
    * _Preparations_ = `part-counterpart` to identify the general nature of the record
    * An [_Individual Count_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#individual-coun) and a [_Description_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#description) to further contextualize what the record represents
    * An image of the cataloged fossil material when possible

##### Historic (legacy) treatments
Although PDWG is working to define best practices for managing data associated with newly curated part-counterpart specimens, in the past, part-counterpart specimens were inconsistently curated across fossil collections; thus, additional guidance is provided below for representing data associated with common scenarios resulting from historic practices. The intention here is provide guidance for capturing this legacy information consistently using Symbiota, but not to imply best practice.

All records representing part-counterpart specimens cataloged in Symbiota should include the data recommended above (all metadata + _Preparations_ = `part-counterpart` + [_Individual Count_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#individual-coun) + [_Description_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#description) + an image (when possible). 

Additionally, the following suggestions are made for several specific scenarios:

**_Pieces of a part-counterpart specimen were cataloged together with suffixed numbers:_**
If pieces of a part-counterpart specimen have been assigned one catalog number with a suffix (such that each piece has an identical catalog number but that number is also associated with a letter or a similar suffix, e.g. "UCM1234a", "UCM1234b", etc), each suffixed piece should be listed in the _Alternative Identifiers_ table. Use `part` or `counterpart` as the _Tag Name_ if specific pieces of the specimen have been explicitly identified as such.

For example:

| Tag Name | Alternative Identifier |
| - | - |
| `part` | `UCM1234a` |
| `counterpart` | `UCM1234b` |

Or:

| Tag Name | Alternative Identifier |
| - | - |
| `part-counterpart` | `UCM1234a` |
| `part-counterpart` | `UCM1234b` |
| `part-counterpart` | `UCM1234c` |
| etc. | etc. |

**_Pieces of a part-counterpart specimen were cataloged separately:_**
Ideally, part-counterpart specimens should be united as one catalog record to avoid confusion for downstream data users (as in the recommended method). However, if this is not possible or practical for some historically curated specimens, once entered into Symbiota, these records can be linked using the Linked Resources tab and the _Relationship Type_ = `partOf`.

**_Pieces of the same organism are owned by multiple institutions:_**
Occasionally, ownership of different pieces of the same individual organism--including but not limited to part-counterpart specimens--may have been divided between institutions. This scenario is generally not advised for newly curated fossils and occasionally occurs in historically curated collections. In these cases, associations can be created between specimen records in your Symbiota portal, as well as to records in other (external) data portals.

**Example:** [USNM PAL 603860](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763802) (cataloged in Symbiota) is a cast of [YPM VP 058990](https://collections.peabody.yale.edu/search/Record/YPM-VP-058990) (cataloged in an external database). An association has been created between these records in Symbiota, whereby:
- _Association Type_ = `Occurrence - External Link`
- _Relationship Type_ = value varies depending on the association to be created

| subjectCatalogNumber | objectID | basisOfRecord | verbatimSciname | resourceURL |
| - | - | - | - | - |
| USNMPAL603860 | YPMVP058990 | FossilSpecimen | Goleroconus alfi | [https://collections.peabody.yale.edu/search/Record/YPM-VP-058990](https://collections.peabody.yale.edu/search/Record/YPM-VP-058990) 

**Tip:** When formatting a spreadsheet for this purpose, the _subjectCatalogNumber_ is the fossil material retained in your collection (cataloged in Symbiota) and the _objectID_ refers to the corresponding material retained in the external collection, as does the _verbatimSciName_.

#### Other cataloging scenarios
The Paleo Data Working Group (PDWG) is actively working to define best practices for the management of fossil specimen data. If you would like guidance on how to treat your fossil specimen data, Symbiota users are strongly encouraged to ask questions in the [PDWG Slack space](/knowledge-hub/community/about-pdwg#get-involved) or bring questions to [PDWG meetings](/knowledge-hub/community/pdwg-happy-hours) for assistance.

### Extending your specimens
Associations can be created between your records in Symbiota and external resource to "extend" your specimen data. Examples include creating links between your records and digitally available literature (e.g. for published specimens) and between your records and other cataloged specimens, both within and external to your Symbiota portal. Creating these associations, or "[extended specimens](/knowledge-hub/explanations/extended-specimen)", can be accomplished two ways:

1) Users with Editor or Administrator permissions can create these linkages one-by-one using the [Linked Resources tab](https://docs.symbiota.org/Editor_Guide/linking_records).

2) Users with Administrator permissions can additionally create these linkages in batch by uploading a CSV-formatted spreadsheet using the [Extended Data Import tool](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources). This option may contain several fields that are not available in the Linked Resources tab, such as _accordingTo_.

{: .notice--warning }
When creating associations with external resources, provide a **stable URL**—like a DOI or a permalink—for the _resourceURL_ whenever possible. Otherwise, your links may eventually break. 

#### Example: Type and referred specimens
You can create linkages between occurrence records in your Symbiota portal and digitally available publications using the fields and parameters specified below.

**Examples:** 1) [USNMV4735](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763793) (holotype of _Ceratosaurus nasicornis_); 2) [USNM P34765](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763783) (specimen of _Carya libbeyii_ that has been referenced in several publications) 
- _Association Type_ = `Non-occurrence Resource`
- _Relationship Type_ = `isReferencedBy`
  
**Option 1: Create links directly in your portal**
_Content forthcoming!_

**Option 2: Create links by uploading a spreadsheet**
Here is an example of what your spreadsheet (CSV) should look like. You can ingest it into your portal using the [Extended Data Import tool](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources).

| subjectCatalogNumber | basisOfRecord | accordingTo | resourceURL |
| - | - | - | - |
| USNMP34765 | ReferenceCitation | Knowlton; 1916; Proceedings of the National Museum | [https://www.biodiversitylibrary.org/page/7764079](https://www.biodiversitylibrary.org/page/7764079) |
| USNMV4735 | ReferenceCitation | Carrano & Choinier; 2016; Journal of Vertebrate Paleontology | [https://doi.org/10.1080/02724634.2015.1054497](https://doi.org/10.1080/02724634.2015.1054497) |

### Data formatting checklist
Before importing existing catalog records into Symbiota, complete this checklist to prepare your data for ingestion. **The aim is to maximize interoperability between records in your dataset and other fossil collections, ultimately making your data more discoverable and useful for research**. The checklist below has been compiled based on commonly encountered scenarios in fossil collections; however, it is not comprehensive and should only serve as a starting point.

{: .notice--success }
When preparing your data, refer to [Symbiota’s Data Import Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) for field definitions, as well as [this page](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/data_import_fields) to learn what types of data can be imported, e.g., which fields can only contain numbers, dates, textual data, etc.

{: .notice--success }
GBIF maintains [an additional list](https://www.gbif.org/data-quality-requirements-occurrences) of data requirements and recommendations to improve data quality and completeness.
 
| Checklist Item | Recommendation |
| - | - |
| **Catalog Numbers** | Every occurrence (catalog record) to be imported must have a unique catalog number. <br>**Example:** `USNMV18414` `ASUCOB0003928` |
| **Basis of Record** | Every record corresponding to cataloged fossil material should receive the [_basisOfRecord_](https://dwc.tdwg.org/terms/#dwc:basisofrecord) value, "FossilSpecimen". <br>**Example:** _basisOfRecord_ = `FossilSpecimen` |
| **Secondary identifiers** | Parse [secondary identifiers](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/catalog_numbers#tag-name--additional-identifier-values--other-catalog-numbers) into a semicolon-delimited list of `key: value` pairs (i.e., tagName: identifier). <br>**Example:** _otherCatalogNumbers_ = `Old Catalog Number: ASU 3541; Accession Number: WIS-L-001456` |
| **Delimiters** | Use pipes (`|`) or semicolons to separate values in lists and be consistent with formatting. Doing so will facilitate parsing of data, if ever needed, in the future. Generally avoid using [commas](https://www.hbs.edu/research-computing-services/data-practices/database-best-practices/delimiters.aspx#:~:text=Word%20of%20Caution%20on%20Delimiters&text=Often%2C%20the%20comma%20is%20used,4%20fields%20instead%20of%203!&text=When%20exporting%20data%2C%20you%20should,also%20occur%20within%20your%20data.) as delimiters. <br>**Example:** _Element_ = `stem | strobilus | root` |
| **Dates** | Fields containing dates should be formatted in [ISO format](https://www.iso.org/iso-8601-date-and-time-format.html), e.g. YYYY-MM-DD. An exception to this rule is [_verbatimEventDate_](https://dwc.tdwg.org/terms/#dwc:verbatimEventDate); use this field when dates are incomplete or not ISO formatted. |
| **Identifications** | For specimens identified above the species level, do not include `sp.`, `indet.`, or similar suffixes. Qualifiers like `aff.` and `?` should be recorded in a separate field, [_identificationQualifier_](https://dwc.tdwg.org/terms/#dwc:identificationQualifier). Verbatim label identifications (e.g. `Lepidophyllum [?]` can be captured in [_identificationRemarks_](https://dwc.tdwg.org/terms/#dwc:identificationRemarks). Leave blank for specimens/specimen lots without identifications. Refer to Symbiota-specific guidance for [_scientificName_ vs. _sciName_](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/data_import_fields). <br>**Example:** _scientificName_=`Phylledestes vorax Cockerell, 1907` or _sciName_=`Phylledestes vorax` |
| **Localities** | If any locality data should be [obscured](https://docs.symbiota.org/Collection_Manager_Guide/Data_Publishing/redacting_obscuring_data/), include a _locationSecurity_ column in your spreadsheet and give records with sensitive locality data a value of “1”. |
| **Geological time** | Refer to Symbiota Docs for important [data field definitions](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#paleontology-fields) and [related instructions](https://docs.symbiota.org/Collection_Manager_Guide/paleo_data). See important notice below regarding **verbatim values in geological context data**.<br>**Example:** _earlyInterval_ = `Late Jurassic` and _lateInterval_ = `Early Cretaceous` |
| **Geological units** | Refer to Symbiota Docs for important [data field definitions](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#paleontology-fields) and see notice below regarding **verbatim values in geological context data**.<br>**Example:** _formation_ = `Wasatch` and _member_ = `Niland Tongue` |
| **Contextual descriptions** | Refer to the field definitions for [_Description_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#description), [_Element_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#element), and [_Individual Count_](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields#individual-count) for important information about how to format data related to anatomy and the physical nature of cataloged fossil material. **Example:** see demo record for [USNMPAL144776](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763845) |
| **Vocabularies** | If your dataset contains anatomical elements that may benefit from the use of a controlled vocabulary, refer to these [examples](https://drive.google.com/drive/folders/1aNHpsLJLuVOubVmbohOZk2VbfDv3BlLH?usp=drive_link). |
| **Cataloging multi-specimen lots** | When multiple individuals of a single taxon exist in a given lot (i.e. isolated in one physical container), they can be cataloged as a single occurrence record. [See below](#cataloging-multi-taxon-specimen-lots) for advice when a lot contains multiple taxa. |
| **Fields containing different kinds of information** | When this is unavoidable, use `key:value` pairs to concatenate data that must be combined into one field. <br>**Example:** _Occurrence Remarks_ = `ACQUISITION DETAILS: Gift of Arthur Lakes April 1890 | NOTES: Original specimen label misplaced`. |
| **Type specimens** | Include a value in [_typeStatus_](https://dwc.tdwg.org/terms/#dwc:typeStatus) ([ICZN](https://www.iczn.org/outreach/faqs/#faq-4) and [IAPT](https://www.iapt-taxon.org/nomen/pages/main/art_9.html) values preferred). [See below](#type-and-referred-specimens) for information about “extending” your specimens that are referenced in literature. |
| **File format** | Save your finalized spreadsheet in comma-separated (CSV) format. Additionally, to ensure any special or accented characters import correctly, always save your data import files using [UTF-8](https://www.w3schools.com/charsets/ref_html_utf8.asp) character encoding. |

{: .notice--warning }
**A note on verbatim values in geological context data:** Many fossil specimens are accompanied by labels, field notes, and other primary data sources containing values that are no longer accepted (e.g. "Tertiary"), informally used (e.g. "Precambrian"), or indicate uncertainty (e.g., "Upper Mio?"). This information is important and should be recorded; however, it cannot be captured using Symbiota's _earlyInterval_ and _lateInterval_ fields, which map to a portal's standardized geological time scale values (by default, these values are based on the [ICS Time Scale](https://stratigraphy.org/chart)). In the absence of an appropriate, standard-based term to record these data, this information should be captured in _stratigraphicRemarks_ as a delimited key:value pair.<br> **[Example](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763806):** `[VERBATIM CHRONOSTRATIGRAPHY: Permian?]` `[VERBATIM GEOLOGICAL CONTEXT: Pittsburgh Coal, Pennsylvanian`
