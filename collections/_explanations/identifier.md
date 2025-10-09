---
title: Identifiers
description: This page explains what types of identifiers are important in the context of paleo data, and how they can be used.
topics: [identifier]
status: published
toc: true
toc_sticky: true
contributors: ["Erica Krimmel"]
last_modified_at: 2025-10-08
---

{: .notice--info }
A version of this content is also [published on the SPNHC wiki](https://spnhc.org/persistent-identifiers/).

As we increasingly digitize specimens and share digital data about our collections, Persistent IDentifiers (PIDs) are often assigned to digital specimen records and can also be used to reference other elements of collections data, such as people or taxa. PIDs are foundational elements of data infrastructure because they enable automated and semi-automated linking between concepts (see {% include resource_link filename='meadows-et-al-2019.yml' %}), and also help make data FAIR, or "findable, accessible, interoperable and reusable" (see {% include resource_link filename='wilkinson-et-al-2016.yml' %}).

## What is a Persistent Identifier?

When we talk about Persistent Identifiers (PIDs) we assume that they are:

- **Unique**. Unlike a catalog number, which may be locally unique, a PID must be unique on the global scale in order to ensure that the object it identifies can be unambiguously referenced. The need for uniqueness means that PIDs must be generated programmatically rather than created by human logic.
- **Persistent**. Once assigned to an object, a PID should never change. PIDs also should not be deleted or reassigned, although in some circumstances a PID may refer to an object that no longer exists. "Never" is still relative; the current systems we use to manage PIDs are expected to have a lifespan of anywhere from decades to centuries.
- **Computer readable**. PIDs are designed primarily for use by computers, not humans, although some PID schemes do have components that are meaningful to humans.
- **Resolvable**. Generally, we expect that a PID can be reliably resolved to a meaningful information about the identified object, e.g., the PID [http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674](http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674) is an actionable URL that redirects to a specimen record on an institutional web portal.

A Universally Unique IDentifier (UUID)–more generically known as a Globally Unique IDentifier (GUID)–is an identifier that is unique, persistent, and computer readable but not resolvable. For example, "3af2b96d2-a8a1-47c5-9895-b0af03b21674" is a UUID and "[http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674](http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674)" is a PID. UUIDs/GUIDs have been widely used by natural history collections to identify digital specimen records in the Darwin Core term dwc:occurrenceID because of how easy they are to acquire via online tools such as [https://www.uuidgenerator.net](https://www.uuidgenerator.net). Although UUIDs/GUIDs will continue to be used and can persist as useful identifiers, the community is moving towards a preference for using true PIDs to reference digital objects such as specimen records. See below for a list of commonly used PID formats and their applications in our domain.  {% include resource_link filename='agosti-et-al-2022.yml' %} also provide an excellent and practical review of how PIDs are being used or should be used by the collections community.

Truly reliable, long term resolvability can be a difficult quality to achieve. Registration agencies are the social infrastructure that govern and maintain resolvability for various PID schemes. For example, DataCite is a registration agency that mints Digital Object Identifiers (DOIs). See {% include resource_link filename='hardisty-et-al-2021.yml' %} for a thorough discussion on what resolvability means and an example of how the European DiSCCo project evaluated PID options for use by its member institutions.

## Types of Identifiers

PIDs (and other identifiers) can be assigned to different types of objects within the realm of natural history collections. Although we often think of them in relation to digital specimen records, PIDs are also useful when assigned to people, organizations, taxonomic concepts and names, geographic places, etc. See the table below for examples of what types of identifiers are most commonly used where, and {% include resource_link filename='von-mering-et-al-2021.yml' %} for further examples.

### Generic identifiers

| Identifier name | Registration/resolution agency | Format & Example value | Comments |
|---|---|----|------|
| ARK (Archival Resource Key) | [ARK Alliance](https://arks.org/) | [URI]+"ark"+[namespace]+[alphanumeric object identifier] <br /><br /> http://n2t.net/ark:/65665/3af2b96d2-a8a1-47c5-9895-b0af03b21674 | ARKs are decentralized, persistent identifiers with the aim of being resolvable via a separate service, N2T. ARKs are a popular solution for identifying collection objects in the museum world. The ARK Alliance is not a true registration agency, as ARKs are created in a decentralized system. Many ARK users are larger libraries or museums with the capacity to mint their own ARKs, although EZID is one example of a registration service provider. May be used as a value in the standard terms dwc:occurrenceID or abcd:unitGUID. |
| GUID (Globally Unique Identifier) | N/A | [alphanumeric object identifier] <br /><br /> fb51580402c14e03bfe0c69437e180ec | A GUID is just a 128-bit integer number generated by an algorithm that is unique enough to make the risk of collision (i.e. generating the same GUID twice) null. A GUID is more generic version of a UUID. Anyone can generate GUIDs for free via online tools such as https://www.guidgenerator.com. A GUID is not inherently resolvable. May be used as a value in the standard terms dwc:occurrenceID or abcd:unitGUID. |
| Universally Unique IDentifier (UUID) | N/A | [alphanumeric object identifier] <br /><br /> fb515804-02c1-4e03-bfe0-c69437e180ec | A UUID is a type of GUID where the format is a string of 32 hexadecimal digits displayed in five groups separated by hyphens. UUIDs should be Version 4. Anyone can generate UUIDs for free via online tools such as https://www.uuidgenerator.net. A UUID is not inherently resolvable. May be used as a value in the standard terms dwc:occurrenceID or abcd:unitGUID. |
| Wikidata QID (Q IDentifier) | [Wikidata](https://www.wikidata.org/) | [URI]+[numeric object identifier] <br /><br /> https://www.wikidata.org/wiki/Q43649390 | Wikidata QIDs can be useful to reference concepts that do not have another, more authoritative source, e.g. a person who collected specimens in the early 1900s but never published anything. Anyone can create or edit Wikidata records, and the data associated with a QID should be expected to constantly evolve. May be used as a value in the standard terms dwc:recordedByID, dwc:identifiedByID, and/or dwc:georeferencedByID. |

### Identifiers commonly used for physical objects

| Identifier name | Registration/resolution agency | Format & Example value | Comments |
|---|---|----|------|
| IGSN (International Generic Sample Number) | [DataCite](https://datacite.org/) | Handle (DOI) <br /><br /> https://doi.org/10.21384/AU1234 | IGSNs are functionally DOIs that are registered in a namespace dedicated to physical samples. Learn more here. May be used as a value in the standard term dwc:materialSampleID. |
| CETAF Stable Identifier | [Consortium of European Taxonomic Facilities (CETAF)](https://cetaf.org/) | [URI]+[alphanumeric object identifier] <br /><br /> http://herbarium.bgbm.org/object/B100277113 or http://www.botanicalcollections.be/specimen/BR0000005516339 or http://data.rbge.org.uk/herb/E00421509 | Typically assigned to specimens in natural history collections. CETAF makes recommendations on the identifier format and qualities, but is not a true registration or resolution agency. Learn more here. May be used as a value in the standard terms dwc:occurrenceID or abcd:unitGUID. |

### Identifiers commonly used for digital objects

| Identifier name | Registration/resolution agency | Format & Example value | Comments |
|---|---|----|------|
| DOI (Digital Object Identifier) | e.g. [DataCite](https://datacite.org/) or [CrossRef](https://www.crossref.org/) | Handle (DOI) <br /><br /> https://doi.org/10.5962/p.304567 | DOIs are a widely used identifier format with multiple registration and resolution agencies. Learn more at the International DOI Foundation. Specimens could be assigned DOIs, but the most common applications for DOIs in our community are digital publications and other documents. |

### Identifiers commonly used for agents (e.g. people, organizations)

| Identifier name | Registration/resolution agency | Format & Example value | Comments |
|---|---|----|------|
| ORCID (Open Researcher and Contributor ID) | [ORCID](https://orcid.org/) | [URI]+[numeric object identifier] <br /><br /> https://orcid.org/0000-0001-6514-963X | ORCIDs use the same format as ISNIs and are used in similar circumstances, except in regards to their creation: whereas asn ISNI may be created on behalf of someone else, an ORCID should only be created by the individual it refers to. If you do not already have an ORCID, you should create one for yourself! May be used as a value in the standard terms dwc:recordedByID, dwc:identifiedByID, and/or dwc:georeferencedByID. |
| ROR (Research Organization Registry identifier) | [Research Organization Registry](https://ror.org/) | [URI]+[alphanumeric object identifier] <br /><br /> https://ror.org/03pnyy777 | ROR is the next generation of a similar identifier type called GRID (Global Research Identifier Database). RORs are designed to identify the top level institution, e.g. a university, and so can be difficult to apply to collections which may be, e.g. a department within a university. |

## Assigning PIDs

How to assign PIDs is a decision that should require careful consideration. See {% include resource_link filename='richards-et-al-2011.yml' %} for a practical discussion on assigning PIDs that continues to be relevant even a decade past its writing (in particular, _Section 5. Checklist for Implementing Persistent Identifiers_). For more on the mechanics of assigning different types of PIDs to different subjects, such as DOIs for taxonomic treatments or INSDC accession numbers for genetic sequences, see see {% include resource_link filename='agosti-et-al-2022.yml' %}.

It is best practice for PIDs to be assigned by the authoritative source, e.g. the institution who created and will manage in perpetuity a digital specimen record, or an individual themselves for a PID referencing a human. It is also important to consider what the identifier is actually representing, e.g. a physical object vs. its digital surrogate, and to document this decision. For example, the European DiSCCo project has determined that in their context PIDs will be assigned to identify the digital representations of physical specimens (see {% include resource_link filename='hardisty-et-al-2021.yml' %}), and a report on PIDs from the Research Data Alliance also recommends assigning them to digital rather than physical objects (see {% include resource_link filename='wittenburg-et-al-2017.yml' %}).

Keep in mind that you can also make use of PIDs that you did not assign. A common example of this is the use of ORCIDs to identify people, like collectors or identifiers, associated with your specimen data.

{% include resource_list topics='identifier' %}
