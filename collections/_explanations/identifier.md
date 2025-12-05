---
title: Identifiers
description: This page explains what types of identifiers are important in the context of paleo data, and how they can be used. A version of this content is also [published on the SPNHC wiki](https://spnhc.org/persistent-identifiers/).
topics: [identifier]
status: published
toc: true
toc_sticky: true
contributors: ["Erica Krimmel"]
last_modified_at: 2025-12-05
---

As we increasingly digitize specimens and share digital data about our collections, Persistent IDentifiers (PIDs) are often assigned to digital specimen records and can also be used to reference other elements of collections data, such as people or taxa. PIDs are foundational elements of data infrastructure because they enable automated and semi-automated linking between concepts (see {% include resource_link filename='meadows-et-al-2019.yml' %}), and also help make data FAIR (see {% include resource_link filename='wilkinson-et-al-2016.yml' %}).

## What is a Persistent Identifier?

When we talk about persistent identifiers, we assume that they are:

- **Unique**. Unlike a catalog number, which may be locally unique, a PID must be unique on the global scale in order to ensure that the object it identifies can be unambiguously referenced. The need for uniqueness means that PIDs must be generated programmatically rather than created by human logic.
- **Persistent**. Once assigned to an object, a PID should never change. PIDs also should not be deleted or reassigned, although in some circumstances a PID may refer to an object that no longer exists. "Never" is relative; the current systems we use to manage PIDs are expected to have a lifespan of anywhere from decades to centuries.
- **Computer readable**. PIDs are designed primarily for use by computers, not humans, although some PID schemes do have components that are meaningful to humans.
- **Resolvable**. Generally, we expect that a PID can be reliably resolved to meaningful information about the identified object, e.g. the PID [http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674](http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674) is an actionable URL that redirects to a specimen record on an institutional web portal.

Truly reliable, long term resolvability can be difficult to achieve. Registration agencies are the social infrastructure that govern and maintain resolvability for various PID schemes. For example, DataCite is a registration agency that mints Digital Object Identifiers (DOIs). See {% include resource_link filename='hardisty-et-al-2021.yml' %} for a thorough discussion on what resolvability means and an example of how the European DiSSCo project evaluated PID options for use by its member institutions.

{: .notice--tip}
Check out these two values to see what resolvable means in practice: "3af2b96d2-a8a1-47c5-9895-b0af03b21674" is a non-resolvable UUID and "[http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674](http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674)" is a resolvable PID.

See below for a list of commonly used identifier formats and their applications in our domain. {% include resource_link filename='agosti-et-al-2022.yml' %} also provide an excellent and practical review of how PIDs are being used or should be used by the collections community. 

## Types of Identifiers

PIDs (and other identifiers) can be assigned to different types of objects within the realm of natural history collections. Although we often think of them in relation to digital specimen records, PIDs are also useful when assigned to people, organizations, taxonomic concepts and names, geographic places, etc. See the table below for a summary of what types of identifiers are most commonly used where, with more detailed explanations following. {% include resource_link filename='von-mering-et-al-2021.yml' %} is a good resource for additional examples.

| Identifier name | Registration/resolution agency | Format & Example value | Use |
|---|---|----|------|
| ARK (Archival Resource Key) | [ARK Alliance](https://arks.org/) | [URI]+[namespace]+[alphanumeric object identifier] <br /><br /> _http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674_ | generic |
| GUID (Globally Unique Identifier) | N/A | [alphanumeric object identifier] <br /><br /> _fb51580402c14e03bfe0c69437e180ec_ | generic |
| Universally Unique IDentifier (UUID) | N/A | [alphanumeric object identifier] <br /><br /> _fb515804-02c1-4e03-bfe0-c69437e180ec_ | generic |
| Wikidata QID (Q IDentifier) | [Wikidata](https://www.wikidata.org/) | [URI]+[numeric object identifier] <br /><br /> _https://www.wikidata.org/entity/Q43649390_ | generic |
| DOI (Digital Object Identifier) | e.g. [DataCite](https://datacite.org/) or [CrossRef](https://www.crossref.org/) | Handle (DOI) <br /><br /> _https://doi.org/10.5962/p.304567_ | digital objects |
| IGSN (International Generic Sample Number) | [DataCite](https://datacite.org/) | Handle (DOI) <br /><br /> https://_doi.org/10.58052/DSR0004SY_ or _igsn:10.58052/DSR0004SY_ | physical objects|
| ORCID (Open Researcher and Contributor ID) | [ORCID](https://orcid.org/) | [URI]+[numeric object identifier] <br /><br /> _https://orcid.org/0000-0001-6514-963X_ | agents |
| ROR (Research Organization Registry identifier) | [Research Organization Registry](https://ror.org/) | [URI]+[alphanumeric object identifier] <br /><br /> _https://ror.org/03pnyy777_ | agents |
| COL identifier | [Catalogue of Life](https://www.catalogueoflife.org) | [namespace]+[alphanumeric object identifier] <br /><br /> _col:4QHKG_ or _col:P_ | taxa |

### Generic identifiers

A Universally Unique IDentifier (UUID)–more generically known as a Globally Unique IDentifier (GUID)–is an identifier that is unique, persistent, and computer readable but **not** resolvable. A GUID is just a 128-bit integer number generated by an algorithm that is unique enough to make the risk of collision (i.e. generating the same GUID twice) null. Anyone can generate GUIDs for free via online tools such as [https://www.guidgenerator.com](https://www.guidgenerator.com). A UUID is a type of GUID where the format is a string of 32 hexadecimal digits displayed in five groups separated by hyphens. Anyone can generate UUIDs for free via online tools such as [https://www.uuidgenerator.net](https://www.uuidgenerator.net).

ARKs (Archival Resource Keys) are decentralized, persistent identifiers with the aim of being resolvable via a separate service, [N2T](https://n2t.net/). They are used in a diversity of contexts, from museum collections to genealogical records to public health documents. The [ARK Alliance](https://arks.org/) is not a true registration agency, as ARKs are created in a decentralized system, and in fact, many ARK users are larger libraries or museums with the capacity to mint their own ARKs. [EZID](https://ezid.cdlib.org/) is one example of a registration service provider.

[Wikidata QIDs](https://www.wikidata.org/wiki/Wikidata:Identifiers) (Q IDentifiers) can be useful to reference concepts that do not have another, more authoritative source, e.g. a person who collected specimens in the early 1900s but never published anything. Anyone can create or edit Wikidata records, and thus the data associated with a QID should be expected to constantly evolve.

### Identifiers for digital objects

Generic identifiers like those described above can be used to reference born-digital objects. A common example is the prevalence of UUIDs/GUIDs or ARKs in the Darwin Core term dwc:occurrenceID.

DOIs are a widely used digital object identifier format with multiple registration and resolution agencies, including [DataCite](https://datacite.org/) and [CrossRef](https://www.crossref.org/). Learn more at the [International DOI Foundation](https://www.doi.org/index.html). Specimens could be assigned DOIs, but the most common applications for DOIs in our community are digital publications and other similarly formal documents.

### Identifiers for physical objects

Generic identifiers like those described above can also be used to reference physical objects, such as fossil specimens or geologic samples. Some identifiers are scoped specifically for referring to physical objects. For example, IGSNs (International Generic Sample Numbers) are functionally DOIs that are registered in a namespace dedicated to physical samples. Users can register samples and get IGSNs via [SESAR](geosamples.org), which is a community platform dedicated to managing and sharing metadata aboout physical samples. Learn about IGSNs [from DataCite](https://support.datacite.org/docs/igsn-ids), which is the parent registration agency that manages IGSNs. 

The Darwin Core terms dwc:materialEntityID and dwc:materialSampleID both expect an identifier such as a UUID/GUID, ARK, or IGSN. Think of these identifiers as a digital complement to human-friendly catalog numbers. 

{: .notice--tip}
Learn more about IGSNs and SESAR from the materials for <a href="{{ '/community/pdwg-happy-hours?topic=2025&topic=identifier' | relative_url }}">PDWG Happy Hour on 2025-10-23</a>.

### Identifiers for agents

Identifiers for agents, such as people or organizations, can be incredibly useful as a means to link out to biographical and other metadata about agents when such data are maintained in a different system from other collections data. Identifiers for agents also help disambiguate agents with the same name, or agents who have changed their name over time. For more about disambiguating agents, check out {% include resource_link filename='bionomia.yml' %}.

For people, identifiers may be used as values in the Darwin Core terms dwc:recordedByID and dwc:identifiedByID. [ORCIDs](https://orcid.org/) are commonly used to identify living people; individuals create an ORCID for themselves rather than being assigned one by a third party. [Wikidata QIDs (Q IDentifiers)](https://www.wikidata.org/wiki/Wikidata:Identifiers) are a generic type of identifier but frequently used for people, both living and dead. Learn more in {% include resource_link filename='bauer-et-al-2022.yml' %}.

For institutions, [ROR (Research Organization Registry)](https://ror.org/) is the next generation of a similar identifier type called GRID (Global Research Identifier Database). RORs are designed to identify the top level institution, e.g. a university, and so can be difficult to apply to collections which may be, e.g. a department within a university.

### Identifiers for taxa

Similarly to identifiers for agents, identifiers for taxa are essential tools to link out to data maintained in other systems, such as taxonomic classifications or nomenclatural history. [Catalogue of Life (COL) identifiers](https://www.catalogueoflife.org/building/identifier) allow the same identifier to be used for the same name across all versions of COL, regardless of monthly, annual or extended releases. The "col" namespace is registered with identifiers.org, so users have to option to reference these in a resolvable way, e.g. [https://identifiers.org/col:4QHKG](https://identifiers.org/col:4QHKG). In Darwin Core, such identifiers may be used with the term dwc:taxonID.

## Assigning PIDs

How to assign PIDs is a decision that should be considered carefully. See {% include resource_link filename='richards-et-al-2011.yml' %} for a practical discussion on assigning PIDs that continues to be relevant even a decade past its writing (in particular, _Section 5. Checklist for Implementing Persistent Identifiers_). For more on the mechanics of assigning different types of PIDs to different subjects, such as DOIs for taxonomic treatments or INSDC accession numbers for genetic sequences, see {% include resource_link filename='agosti-et-al-2022.yml' %}.

It is best practice for PIDs to be assigned by the authoritative source, e.g. the institution who created and will manage in perpetuity a digital specimen record, or an individual for a PID referencing themself. It is also important to consider what the identifier is actually representing, e.g. a physical object vs. its digital surrogate, and to document this decision. For example, the European DiSSCo project has determined that in their context PIDs will be assigned to identify the digital representations of physical specimens (see {% include resource_link filename='hardisty-et-al-2021.yml' %}), and a report on PIDs from the Research Data Alliance also recommends assigning them to digital rather than physical objects (see {% include resource_link filename='wittenburg-et-al-2017.yml' %}).

Keep in mind that you can also make use of PIDs that you did not assign. A common example of this is the use of ORCIDs to identify people, like collectors or identifiers, associated with your specimen data.

{% include resource_list topics='identifier' %}
