---
title: Manage data about taxonomy
status: draft
topics:
- manage data
- taxonomy
---

# Content to expand on

Taxonomic data are stored differently in different [Collections Management Systems](). Options include:
- Multiple flat hierarchical trees for each taxon (Arctos, Symbiota)
- Hierarchy through parent-child relationships, with stepchildren / synonyms (MS SQLServer, Specify)
- Hierarchy through parent-child relationships (EMu, Specify)
- Fields for each rank that are not connected - flat structure (MCZbase, Access)
- Pseudo-hierarchy - not explicitly linked across entries in tree (EMu - NMNH)

Taxonomic authorities are a critical resource for collections management because they provide information about valid and invalid names curated by taxonomic experts. Different general strategies for using taxonomic authorities include:
- For a given species identification in the collection, use the taxonomic authority to get information about higher taxonomy, e.g. family level and above.
- Look up synonymous names in the taxonomic authority.
- Create a custom taxonomic dictionary on other existing taxonomy authorities.
- Track opinions from taxonomic authority as a way to provide more information about the validity (or lack thereof) of specimen identifications.
- Include links to identifiers maintained by a taxonomic authority (e.g. AphiaIDs from WoRMS) for taxon concepts

Including scientific authorship alongside the taxonomy for species-level identifications is a common practice in paleo collections, and an important way to disambiguate homonyms across the broader landscape of neontological and fossil taxonomy.

Across paleo collections, we lack a good method for dealing with higher classification for taxa where this is unknown, e.g. for many ichnofossils. The most common strategy is to leave fields related to higher classification blank, although some collections prefer to record "incertae sedis, "or "indet."/"indeterminate" in these fields. The ICZN (1999) recognizes "incertae sedis" but recommends attaching the highest known taxonomic level, e.g. "Cephalopoda incertae sedis." 

Unranked clades also pose a challenges in fossil taxonomy. Not only are many databases unable to handle the data structure of unranked clades, but it can also be hard to determine how many clades a specimen belongs to. Furthermore, clades intersect with Linnean taxonomy in varied and often inconsistent ways. Currently, many paleo collections are managing data about unranked clades eitey by shoehorning them into fields designed for Linnean taxonomy or into a notes field. Both of these options limit discoverability.

Identification qualifiers–such as "cf.", "aff.", "sp. A," "sp. etxc.", etc.– are especially important in paleo collections. Figure 1 in [Sigovini et al. 2016](../_data/resources/sigovini-et-al-2016.yml) offers a good framework for how to use qualifiers in taxonomy.

# Resources for taxonomy

## Higher taxonomy across fossil taxonomic groups

{% include resource_card filename='worms.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='col.yml' %}
{% include resource_card filename='pbdb.yml' %}
{% include resource_card filename='itis.yml' %}
{% include resource_card filename='bugguide.yml' %}

## Micropaleontology
See Paleobotany (below) for pollen and spores.

{% include resource_card filename='foraminifera.yml' %}
{% include resource_card filename='worms.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='col.yml' %}
{% include resource_card filename='pbdb.yml' %}

## Ichnology/Trace fossils

{% include resource_card filename='carpenter-et-al-1994.yml' %}
{% include resource_card filename='lockley-peterson-2003.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='pbdb.yml' %}

## Invertebrate paleontology

{% include resource_card filename='treatise-ip.yml' %}
{% include resource_card filename='bouchet-et-al-2010.yml' %}
{% include resource_card filename='bouchet-et-al-2017.yml' %}
{% include resource_card filename='carter-et-al-2011.yml' %}
{% include resource_card filename='coan-et-al-2000.yml' %}
{% include resource_card filename='coan-scott-2012.yml' %}
{% include resource_card filename='texas-cretaceous.yml' %}
{% include resource_card filename='blake-lissner-1996.yml' %}
{% include resource_card filename='ponder-et-al-2020.yml' %}
{% include resource_card filename='worms.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='col.yml' %}
{% include resource_card filename='pbdb.yml' %}

## Paleobotany
Including palynology.

{% include resource_card filename='ifpni.yml' %}
{% include resource_card filename='ipni.yml' %}
{% include resource_card filename='index-fossil-plants-1.yml' %}
{% include resource_card filename='index-fossil-plants-2.yml' %}
{% include resource_card filename='index-fossil-plants-3.yml' %}
{% include resource_card filename='index-fossil-plants-4.yml' %}
{% include resource_card filename='genera-fossil-spores.yml' %}
{% include resource_card filename='algaebase.yml' %}
{% include resource_card filename='bryonames.yml' %}
{% include resource_card filename='species-fungorum.yml' %}
{% include resource_card filename='pteridoportal.yml' %}
{% include resource_card filename='bhl.yml' %}
{% include resource_card filename='worms.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='col.yml' %}
{% include resource_card filename='pbdb.yml' %}
{% include resource_card filename='itis.yml' %}

## Vertebrates

{% include resource_card filename='.yml' %}
{% include resource_card filename='worms.yml' %}
{% include resource_card filename='irmng.yml' %}
{% include resource_card filename='col.yml' %}
{% include resource_card filename='pbdb.yml' %}

{% include resource_list topics='taxonomy' %}
