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

Identification qualifiers–such as "cf.", "aff.", "sp. A," "sp. etxc.", etc.– are especially important in paleo collections. Figure 1 in [Sigovini et al. 2016](sigovini-et-al-2016.yml) offers a good framework for how to use qualifiers in taxonomy.

{% include resource_list topics='taxonomy' %}
