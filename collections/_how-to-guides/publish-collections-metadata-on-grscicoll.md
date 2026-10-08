---
title: Publish collections metadata on GRSciColl
description: This page contains detailed instructions for publishing metadata about fossil collections on the Global Registry of Scientific Collections (GRSciColl), and also links out to related resources.
topics: [grscicoll, inventory]
status: published
contributors: ["Erica Krimmel", "Lindsay Walker"]
last_modified_at: 2026-10-08
---

Collections metadata is an important way for researchers to discover potentially relevant specimens, especially since many fossil collections have large backlogs of unprocessed and yet-to-be-digitized material. Registries for collections metadata are not new–see e.g. {% include resource_link filename='webby-1989.yml' %}–but they have become increasingly accessible in the digital age. The Global Registry of Scientific Collections (GRSciColl) is currently one of the most comprehensive such registries, and publishing collection metadata here can help others discover you.

{: .notice--info }
For an example of a well-populated institutional record on GRSciColl, see the [University of Colorado Museum of Natural History](https://scientific-collections.gbif.org/institution/1a81a175-787f-4e26-9139-1b4203b76d8d). For an example of a well-populated collection record, see the [Palaeontology collections at MNHN Luxembourg](https://scientific-collections.gbif.org/collection/855f343c-93d6-4333-95c8-3bdc58d9e95c).

GRSciColl has [detailed video tutorials](https://scientific-collections.gbif.org/how-to) for how to navigate the registry and update its content, including adding a new institution or collection. Their [FAQ page](https://scientific-collections.gbif.org/faq) is also very helpful. The instructions on this page complement GRSciColl's content with recommendations specific to fossil collections.

{: .notice--tip }
When creating new records or editing existing GRSciColl records, in practice, first you will be _suggesting_ changes to the Registry, which in turn will be reviewed by one of GRSciColl's regional editing teams. You may be contacted by a GRSciColl Editor if they have questions about your changes to the registry before your changes become publicly visible.

## Check to see if your collection or institution already exists

Data in GRSciColl originated from previous efforts to aggregate collections metadata, so there is a good chance your institution and/or collection already exist in the registry.

1. First [search for your institution](https://scientific-collections.gbif.org/institution/search). Use increasingly broad search terms, like part of the institution's name or the city the institution is located in, to confirm if you think your institution is not already in the registry.
1. If you found your institution, your collection may be linked from the institutional entry. If you did not find your institution or your collection did not appear connected to the institution, [search for your collection](https://scientific-collections.gbif.org/collection/search) next. Try searching by your collection code, variations on its name, and location to confirm if you think your collection is not already in the registry.
1. If you cannot find your institution and/or collection, follow [GRSciColl's instructions](https://scientific-collections.gbif.org/how-to) to create a new entry for either/both.

## Verify or add content type to collection records

GRSciColl uses "content type" tags to group collections by discipline. Fossil collections should include one or more of the following content type tags:  `vertebrate fossils`, `invertebrate fossils`, `plant fossils`, `trace fossils`, `invertebrate microfossils`, `conodonts`, `petrified wood`. Any of these more specific tags will be discoverable under the broader content type `Paleontological`, which you can also use if more specific types don't make sense for your collection.

## Verify or add essential contact information

Contact details are an important bridge between people discovering that your collection exists, and actually being able to reach out if they want to use or learn more about the collection. Contacts also become easily out-of-date with staff turnover. For this reason, and when feasible, it is helpful to include multiple contacts and/or a generic organizational email (e.g. paleo@yourinstitution.org).

1. Verify any existing contact information at both the institution and collection level.
1. Add physical location addresses, staff roles, and emails where appropriate. Staff can have metadata about their taxonomic expertise included, if relevant.
1. Note that although many collection contacts also appear on the institutional contact list, the institution record does not automatically inherit contacts from each of its collections.

## Connect your GRSciColl records with data published on GBIF

If you publish specimen data from your collection to GBIF, it should be linked to your collection record on GRSciColl. For an example of what this looks like, see the [Paleontological Research Institution's collection](https://scientific-collections.gbif.org/collection/5cbcdbf4-d25c-45e6-92c8-58e197988a2e):

{% include figure popup=true image_path="/assets/images/grscicoll-pri.png" alt="screenshot of the PRI collection record" caption="Screenshot of the PRI collection record on GRSciColl illustrating how it looks when specimen records on GBIF are correctly linking." %}

If your specimen data are not showing up, you can fix this by adding the URL for your collection and institution in GRSciColl to your specimen data via (respectively) the Darwin Core fields for {% include glossary term="institutionID" namespace="dwc" %} and {% include glossary term="collectionID" namespace="dwc" %}. Learn more from the [GRSciColl FAQs here](https://scientific-collections.gbif.org/faq#how-to-link-specimen-related-occurrences-published-on-gbif-to-grscicoll-entries).

## Add details via collection descriptors

Collection descriptors are meant to share structured information about collections, such as that which might be [captured in a collection inventory](/how-to-guides/capture-inventory-data). This type of information might be particularly relevant to share via GRSciColl for collections that aren’t fully digitized and/or where specimen records aren’t available online. Learn more about [how GRSciColl can help make this type of data discoverable](https://data-blog.gbif.org/post/grscicoll-collection-descriptors), and see an example of [an herbarium with robust collection descriptor data](https://scientific-collections.gbif.org/collection/6416a67f-3c3e-495c-8998-568f64249178).

{% include resource_list topics='grscicoll' %}
