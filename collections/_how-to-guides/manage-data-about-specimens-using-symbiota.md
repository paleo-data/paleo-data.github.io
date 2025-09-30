---
title: Manage data about fossil specimens using Symbiota
description: 'This guide is intended to complement [introductory documentation](/how-to-guides/start-using-symbiota) for Symbiota data providers, as well as the official Symbiota user documentation, [Symbiota Docs](https://docs.symbiota.org). Symbiota Docs provides general guidance for working in Symbiota-based data portals and should be referenced for basic functions and workflows. This manual expands on this resource to provide discipline-specific information for fossil collections.'
topics: [symbiota, extended specimen]
sidebar:
  nav: [sidebar]
  collapsible: true
  expanded: [how-to-guides]
toc: true
toc_sticky: true
status: published
contributors: ["Lindsay Walker"]
last_modified_at: 2025-09-29
---

## Introduction
There are two ways specimen records are typically entered into a Symbiota portal: 1) as a [bulk data import](#bulk-data-import) or 2) [directly using the Occurrence Editor interface](#direct-data-entry). Additional methods exist, but these are the most commonly used options by collections that actively ("live") manage their specimen data using Symbiota. In all cases, the end goal is to make your data more easily managed, discovered, and used for research; thus, data providers are strongly encourged to follow the steps outlined in this how-to guide.

Regardless of data entry method, it is important that all data providers become familiar with the [Darwin Core data standard](https://dwc.tdwg.org/terms/), which forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields).

## Bulk data import
This section outlines actions you can take to prepare and import (ingest) existing digital catalog records from your fossil collection into a Symbiota portal.

**1. Prepare your records for import:** <br>
- If you maintain existing catalog records to be imported into Symbiota, perform some data cleaning to align your records to Symbiota's data fields and formatting requirements. The [data formatting checklist](#data-formatting-checklist) and [example records][#example-records] are intended to inform this process, and [OpenRefine](https://openrefine.org) is free software that can be used for this purpose. Additional data cleaning can be performed once your records have been imported into Symbiota.
- If you’d like a template to follow, [this spreadsheet](https://docs.google.com/spreadsheets/d/1b1aN6NuoOEN4IlToV3Uk33xpSwrbcn3-uceSnlgf8JI/edit?usp=sharing) is preformatted for use with Symbiota. Your spreadsheet must be converted to CSV format (use UTF-8 character encoding) prior to ingestion into the portal, which can be easily accomplished in a program like [Microsoft Excel](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) or [Google Sheets](https://support.google.com/docs/answer/49114?sjid=17532513690429081890-NC). An expanded version of this spreadsheet can be provided [upon request](mailto:paleoinformatics@gmail.com).

{% include resource_card filename='krimmel-walker-2022.yml' %}
{% include resource_card filename='krimmel-2022-data-wrangling.yml' %}

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
The content in this section outlines recommendations for direct data entry using Symbiota's Occurrence Editor interface, which allows users with Administrator and Editor user permissions to add and edit specimen records in Symbiota. As a reminder, the [Darwin Core data standard](https://dwc.tdwg.org/terms/) forms the basis for the majority of [Symbiota’s Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields), and a series of [example records](#example-records) has been created to guide data entry.

<iframe src="https://docs.google.com/presentation/d/1yJFsaCnBC28zW8UtLfl3tnJayk3w-BRDtVzyZYpD1TI/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Data maintenance
Once your records are imported or entered directly into Symbiota, some effort will be required to correct, maintain, or improve the quality of your specimen data. These activities are important to keeping your records easily managed, discoverable, and useful for research. The following recommendations are made to help you begin this process. 

**Prevent new errors** <br>
When training new staff or volunteers on data entry or management, it is **highly** recommended that you point them toward this Knowledge Hub, but more specifically, have them become familiar with the [Symbiota Data Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) and the [data formatting checklist](#data-formatting-checklist).

**Mitigate existing errors** <br>
Mistakes are likely to happen, even in carefully curated datasets. It is therefore recommended that you routinely assess your data using the [Symbiota Data Quality Toolkit](https://biokic.github.io/symbiota-docs/editor/quality/). This guide is designed to enable users with either Administrator or Editor permissions to your Collection Profile to “clean” your data–i.e. find and correct errors–using the portal’s built-in features wherever possible.

**Crowdsource quality control** <br>
Symbiota maintains several built-in tools to facilitate collaborative data entry and data cleaning when enabled for your collection.  For example, Administrators of a given collection can enable any portal user who is logged in with an account to suggest edits to your records in the portal. Suggestions must be reviewed by an Administrator before they become public. By default, this option is turned **off**, but it can be activated through your Administrator Control Panel. Review [Symbiota Docs](https://docs.symbiota.org/Collection_Manager_Guide/Comments_Feedback/public_edits/) for more information about this feature. 

**Set up a data import profile** <br>
If you intend to routinely import data using a standard import template--for example, if you intend to cataloging using a spreadsheet method--you can set up a new data [import profile](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/#initiating-the-upload) based on your cleaned spreadsheet.

## Appendices

### Data formatting checklist
Before importing existing catalog records into Symbiota, complete this checklist to prepare your data for ingestion. **The aim is to maximize interoperability between records in your dataset and other fossil collections, ultimately making your data more discoverable and useful for research**. The checklist below has been compiled based on commonly encountered scenarios in fossil collections; however, it is not comprehensive and should only serve as a starting point.

{: .notice--success }
When preparing your data, refer to [Symbiota’s Data Import Fields](https://docs.symbiota.org/Editor_Guide/Editing_Searching_Records/symbiota_data_fields) for field definitions, as well as [this page](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/data_import_fields) to learn what types of data can be imported, e.g., which fields can only contain numbers, dates, textual data, etc.

{: .notice--success }
GBIF maintains [an additional list](https://www.gbif.org/data-quality-requirements-occurrences) of data requirements and recommendations to improve data quality and completeness.
 
| Checklist Item | Recommendation |
| - | - |
| **Catalog numbers** | Every occurrence (catalog record) to be imported must have a unique catalog number. <br>**Example:** `USNMV18414` `ASUCOB0003928` |
| **Basis of record** | Every record corresponding to cataloged fossil material should receive the [_basisOfRecord_](https://dwc.tdwg.org/terms/#dwc:basisofrecord) value, "FossilSpecimen". <br>**Example:** _basisOfRecord_ = `FossilSpecimen` |
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
**A note on verbatim values in geological context data:** Many fossil specimens are accompanied by labels, field notes, and other primary data sources containing values that are no longer accepted (e.g. "Tertiary"), informally used (e.g. "Precambrian"), or indicate uncertainty (e.g., "Upper Mio?"). This information is important and should be recorded; however, it cannot be captured using Symbiota's _earlyInterval_ and _lateInterval_ fields, which map to a portal's standardized geological time scale values (by default, these values are based on the [ICS Time Scale](https://stratigraphy.org/chart)). In the absence of an appropriate, standard-based term to record these data, this information should be captured in _stratigraphicRemarks_ as a delimited key:value pair.<br> **[Example](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763806):** `[VERBATIM CHRONOSTRATIGRAPHY: Permian?]`

### Example records
Fossil specimens present many scenarios that can be challenging to translate into informative catalog records. The following example records are intended to illustrate how to represent fossil specimen data using Symbiota. These records are expected to evolve as best practices for managing and publishing fossil specimen data are formalized. 

{: .notice--success }
If you would like guidance on how to treat your fossil specimen data, Symbiota users are strongly encouraged to ask questions in the [PDWG Slack space](/community/about-pdwg#get-involved) or bring questions to [PDWG meetings](/community/pdwg-happy-hours) for assistance. You are also welcome to contact the Paleo Data Portal's [Steering Committee](https://paleo.symbiota.org/portal/misc/contacts.php) for input.

Some of the following records include redacted data (images and locality details); please contact [paleoinformatics@gmail.com](mailto:paleoinformatics@gmail.com) if you require more information about these records. Additionally, for ease of reference, these examples are organized by collection subdiscipline (e.g., "IP" = Invert Paleo, "VP" = Vert Paleo, etc.); however, many of these examples will apply across collection categories.

|Category|Example Record Description                                                                    |Record |
|--------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|IP      |one taxon, one individual                                                      |[USNMMO647519](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763848) |
|IP      |one taxon, multiple individuals                                                   |[USNMPAL665453](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763837)|
|IP      |slab: multiple taxa, multiple individuals                                         |[USNMPAL83927](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763831) & [USNMPAL188127](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763832) |
|IP      |slab: multiple taxa, multiple individuals (all cataloged)                         |[USNMPAL449450](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763833) & assoc. records|
|IP+PB   |slab: multiple taxa, multiple individuals (some uncataloged)              |[USNMPAL566311](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763846)|
|PB      |one lot, one individual, part-counterpart pair - one number                       |[USNMP42726](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763830)   |
|PB      |one lot, one individual, part-counterpart pair - multiple numbers                 |[USNMP7427](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763803) & [USNMP7428](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763829)   |
|VP      |one taxon, one individual, isolated element                                       |[USNMV8814](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763812)    |
|VP      |one taxon, whole articulated skeleton - composite                                 |[USNMV6721](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763813)    |
|VP      |one taxon, whole articulated skeleton - composite                                 |[USNMV10304](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763814) & assoc. records|
|VP      |slab: single taxon, multiple pieces of one individual                             |[USNMV22753](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763821)   |
|VP      |slab: single taxon, multiple pieces of one individual                             |[USNMV2395](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763822)    |
|VP      |slab: bone bed, multiple individuals - multiple numbers                           |[USNMV21375](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763823) & [USNMPAL606789](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763824)   |
|VP      |cast and fossil, one individual                                                   |[USNMV6720](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763826)    |
|VP      |cast and fossil, one individual                                                   |[USNMPAL215070](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763827)|
|VP      |cast and fossil, one individual                                                   |[USNMV6527](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763847)    |
|VP      |cast of another institution specimen                                              |[USNMPAL299545](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763828)|
|VP      |ichnofossil (coprolite)                                                           |[USNMPAL617525](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763825)|

### Extending your specimens
Associations can be created between your records in Symbiota and external resource to "extend" your specimen data. Examples include creating links between your records and digitally available literature (e.g. for published specimens) and between your records and other cataloged specimens, both within and external to your Symbiota portal. Creating these associations, or "[extended specimens](/explanations/extended-specimen)", can be accomplished two ways:

1) Users with Editor or Administrator permissions can create these linkages one-by-one using the [Linked Resources tab](https://docs.symbiota.org/Editor_Guide/linking_records).

2) Users with Administrator permissions can additionally create these linkages in batch by uploading a CSV-formatted spreadsheet using the [Extended Data Import tool](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources). This option may contain several fields that are not available in the Linked Resources tab, such as _accordingTo_.

#### Example: Type and referred specimens
You can create linkages between occurrence records in your Symbiota portal and digitally available publications using the fields and parameters specified below.

**Examples:** 1) [USNMV4735](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763793) (holotype of _Ceratosaurus nasicornis_); 2) [USNM P34765](https://paleo.symbiota.org/portal/collections/individual/index.php?occid=763783) (specimen of _Carya libbeyii_ that has been referenced in several publications) 
- _Association Type_ = `Non-occurrence Resource`
- _Relationship Type_ = `isReferencedBy`
  
**Option 1: Create links directly in your portal** <br>
To create a link to a digitially available non-occurrence resource external to your portal, such as a publication, used the Occurrence Editor form's Linked Resources tab as shown below.

<img style="float: center; margin: 0px 0px 0px 0px;" width="90%" src="/assets/images/symbiota_linkedresource-literatureexample.png" alt="Symbiota Linked Resources tab" caption="Links to external resources, like pubished literature, can be created directly in the portal using the Linked Resources tab.">

{: .notice--warning }
When creating associations with external resources, provide a **stable URL**—like a DOI or a permalink—for the _resourceURL_ whenever possible. Otherwise, your links may eventually break. 

**Option 2: Create links by uploading a spreadsheet** <br>
Here is an example of what your spreadsheet (CSV) should look like. You can ingest it into your portal using the [Extended Data Import tool](https://docs.symbiota.org/Collection_Manager_Guide/Importing_Uploading/linked_resources).

| subjectCatalogNumber | basisOfRecord | objectID | resourceURL |
| - | - | - | - |
| USNMP34765 | Reference Citation | Knowlton; 1916; Proceedings of the National Museum | [https://www.biodiversitylibrary.org/page/7764079](https://www.biodiversitylibrary.org/page/7764079) |
| USNMV4735 | Reference Citation | Carrano & Choinier; 2016; Journal of Vertebrate Paleontology | [https://doi.org/10.1080/02724634.2015.1054497](https://doi.org/10.1080/02724634.2015.1054497) |
