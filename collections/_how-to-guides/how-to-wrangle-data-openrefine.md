---
title: Wrangle data in OpenRefine
last_modified_at: 2025-07-08
authors: ["Erica Krimmel"]
topics: [data wrangling, workflows]
---

[OpenRefine](https://openrefine.org/) is a free, open-source tool for manipulating small or large datasets in numerous formats (CSV, JSON, XML, etc.). Because of its low barrier to entry with no prior programming knowledge needed, OpenRefine is an excellent tool for the improvement and maintenance of data integrity for best practices in collections management. Data transformations are reversible and repeatable, and original data are locally preserved. OpenRefine runs locally on your computer, it is ideal for use with sensitive data and/or no internet connection.  The learning curve for OpenRefine is moderate, with a large community of users and shared knowledge base for help. You can use the resources here as a starting point! 

**When to use OpenRefine**
- For quality control, e.g. to clean recent data entry prior to (or after) database ingestion, or to clean legacy data.
- For combining and manipulating existing datasets, e.g. to transform or integrate your data with external resources like those in a taxonomic authority or Wikidata.

**When not to use OpenRefine**
- For adding new records individually to an existing dataset, e.g. when transcribing specimen labels.
- For text-heavy one-off data entry, e.g. when typing a sentence in a notes field associated with each row.
- For projects with multiple users on separate computers.

{% include resource_card filename='krimmel-walker-2022.yml' %}

# Getting started

Download OpenRefine from https://openrefine.org.

# Basic tutorials

See links below for our recommended tutorials on how to use OpenRefine. OpenRefine itself maintains a more comprehensive list of [externally produced tutorials here](https://github.com/OpenRefine/OpenRefine/wiki/External-Resources), and searching on [YouTube](https://www.youtube.com/results?search_query=openrefine) and [Vimeo](https://www.youtube.com/results?search_query=openrefine) will also lead to many relevant videos.

- Data Carpentry lessons: [OpenRefine for Natural History Collection Data](https://www.youtube.com/results?search_query=openrefine) and [Data Cleaning with OpenRefine for Ecologists](https://datacarpentry.org/OpenRefine-ecology-lesson/)
- Library Carpentry lesson: [OpenRefine](https://datacarpentry.org/OpenRefine-ecology-lesson/)
- [OpenRefine Walk-through](http://bit.ly/BITW13_OpenRefine), step-by-step orientation by Javier Otegui using natural history museum data as a subject
- [Clean Your Data: Getting Started with OpenRefine](https://www.youtube.com/watch?v=wGVtycv3SS0), a workshop recording produced by the University of Idaho Library Digital Initiatives (2017-02-15)
- Handouts created for use during the 2019 VRA Annual Conference workshop, _Clean, Transform and Enhance Your Data_: [Download and Install OpenRefine](https://docs.google.com/document/d/1Z863T411TKd1FnmKrbEAERCPHNzxj4enscjTe3OnfgM/edit?usp=sharing) and [Getting Started with OpenRefine](https://docs.google.com/document/d/1fH_kqo5QtrovLk63uRf4ixScMMy-jO5IikrCOeZl6JM/edit?usp=sharing)
- [Data Cleaning with OpenRefine](https://www.youtube.com/watch?v=6DIsErw8noM), and online short seminar organized by the Harvard Library (2020-06-25)

# Reconciliation

Reconciliation in OpenRefine allows you to look up values from your dataset in an external source, such as Wikidata. When you reconcile a value, OpenRefine can use fuzzy matching to find multiple possibly options for which value in the external source yours matches with. You can then select the appropriate match and pull additional values into your dataset from the external source based on the match. Learn more about [reconciliation from the OpenRefine documentation here](https://docs.openrefine.org/manual/reconciling), and see [this list of additional sources offering reconciliation services through OpenRefin](https://reconciliation-api.github.io/testbench/#/)e.

# Scripting

OpenRefine enables a variety of options for using scripting to extend the functionally of its graphical user interface. The main scripting languages used are General Refine Expression Language (GREL), which is similar to Excel string formulas, and Python. It can also be helpful to familiarize yourself with JavaScript Object Notation (JSON), which is a common data-interchange format.

## Handy GREL scripts

- To trim leading and trailing whitespace, navigate to _Edit cells > Transform_ and use the following code: `value.trim()`. This functionality can also be accomplished without scripting by navigating to _Edit cells > Common transforms > Trim leading and trailing whitespace_.

- To collapse whitespace, e.g. a double space or a return carriage, navigate to _Edit cells > Transform_ and use the following code: `value.replace(/\s+/,' '). This functionality can also be accomplished without scripting by navigating to _Edit cells > Common transforms > Collapse consecutive whitespace_.

- To add the same text to every selected row in a column with existing values, navigate to _Edit cells > Transform_ and use the following code: `"NEW-TEXT" + value`

- To replace text in a column, navigate to _Edit cells > Transform_ and use the following code: `value.replace("EXISTING-VALUE","NEW-VALUE")`. This functionality can also be accomplished without scripting by navigating to _Edit cells > Replace_.

- To concatenate values from multiple columns, from the first column navigate to _Edit cells > Transform_ and use the following code: `value + cells["SECOND-COLUMN"].value + cells["THIRD-COLUMN"].value`. You can combine this feature with the ability to add text, e.g. `"NEW-TEXT" + value + cells["SECOND-COLUMN"].value`, and this functionality can also be accomplished without scripting by navigating to _Edit column > Join columns..._

- To convert data in date format into a simplified text format, navigate to _Edit cells > Transform_ and use the following code: `value.toDate().toString('YYYY-MM-dd')`

- To bring data from one OpenRefine project into a second OpenRefine project, from the second project navigate to _Edit column > Add column based on this column_ and use the following code: `cell.cross("NAME-OF-PROJECT-1", "PROJECT-1-COLUMN-TO-MATCH-ON")[0].cells["PROJECT-1-COLUMN-TO-GET-VALUE-FROM"].value`

- To add a facet based on whether or not the values in a row match between two columns, navigate to _Facet > Custom text facet_ and use the following code: `cells["COLUMN-1"].value[0] == cells["COLUMN-2"].value[0]`

- To use Google Maps to reverse geocode place names in your data (e.g. to look up and retrieve geospatial and administrative data about an address or a local landmark), navigate to _Edit column > Add column based on this column_ and use the following code: `https://maps.googleapis.com/maps/api/geocode/json?latlng="+value+"&key=KEY`. You need an API key to use this service; [learn more about how to get one here](https://developers.google.com/maps/documentation/javascript/get-api-key).

- To parse the results of Google Maps reverse geocoding, navigate to _Edit cells > Transform_ and use the following code: `forEach(value.parseJson().results[0].address_components,x,[x.types[0], x.long_name].join("::")).join("|")`.

# Join the community

There are many audiences for OpenRefine, and the best community to join is one that aligns with your usage context and skill level. The OpenRefine Google Group is maintained by OpenRefine, and most messages posted are more technical. 
