---
title: Develop a digitization workflow using Symbiota
last_modified_at: 2025-06-03
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
topics: [symbiota]
---

{: .notice--primary }
This guide is intended to help data providers develop digitization workflows for fossil specimens using Symbiota.

# Introduction

## Digitization workflows for fossil collections
In the context of this guide and other Knowledge Hub documentation, "digitization" is act of translating and capturing metadata describing a physical specimen into a digital form ([Nelson & Ellis, 2018](https://doi.org/10.1098/rstb.2017.0391)). It can encompass tasks related to [cataloging](#cataloging), [georeferencing](#georeferencing), and [imaging](#imaging). 

Many paleontological collections are highly heterogeneous in nature--taxonomically, geographically, geologically, and physically. That is, one collection might contain both long-extinct and geologically recent organisms and their traces, including vertebrates, invertebrates, and plants of varying sizes and shapes and in various states of physical preparation.

Careful planning is necessary to efficiently digitize fossil specimen data in paleontological collections, and workflow development a critical part of this process. By designing and streamlining a thoughtful digitization workflow, you can maximize your collection’s visibility and application for research and educational use, in turn generating further justification for its ongoing maintenance to administrators, prospective funders, and other potential stakeholders.

### Where to start 
Start by defining the goal of your digitization workflow. For instance, do you need to capture specimen records for a specific research project, or is your aim to document core specimen data to make your collection more discoverable? Defining the end goal will allow you to prioritize various workflow elements and digitization tasks given the nature of your collection and its available resources. The content in this guide is designed to facilitate the creation of workflows that output discoverable, interoperable data in the context of the [Paleo Data Ecosystem](/knowledge-hub/data-ecosystem).

Symbiota software is particularly well-suited to is enabling flexible digitization workflows to quickly increase the digital presence of your collection, for example, by facilitating the creation of skeletal specimen records that can be iteratively improved upon as time and resources allow. The content in this guide is tailored to data providers who wish to create Symbiota-based digitization workflows and is intended to be read in parallel with the Knowledge Hub’s various [Symbiota how-to guides](/knowledge-hub/topics?topic=symbiota) and related content.

# Workflow components

## Cataloging

Sometimes "cataloging" is used interchangably with "trasncription" and "databasing". 

Because data transcription inherently involves judgement calls, and not all label data can be accurately represented using existing data standards, imaging specimen label images is recommended whenever possible. 

## Georeferencing

Georeferencing can be defined as "the process (verb) or product (noun) of interpreting a locality description into a spatially mappable representation using a georeferencing method" ([Zermoglio et al., 2020](https://docs.gbif.org/georeferencing-quick-reference-guide/1.0/en/#georeference)). Georeferencing can be a signficiant component of a digitization workflow; for example, it is often required to assign geographic coordinates to historically collected specimens. Symbiota portals contain a number of built-in tools to facilitate georeferencing on a record-by-record basis, in batch, or collaboratively. Many resources exist that explain georeferencing and how related tools work in Symbiota portals.

### Symbiota-specific resources
- [Overview of georeferencing tools in Symbiota](https://youtu.be/5DmgrjmHYJ8?si=xsW70OSa_1ta86Sa&t=691)
- [Georeferencing in CCH2 [a Symbiota portal] training course](https://www.capturingcaliforniasflowers.org/georeferencingcourse.html)

### General georeferencing resources
- [TDWG Earth Science and Paleobiology Interest Group georeferencing resources for paleontological collections](https://tdwg.github.io/esp/georeferencing/README.html)
- [Georeferencing Quick Reference Guide](https://doi.org/10.35035/e09p-h128)
- [Georeferencing in CoGe training video](https://youtu.be/h1JfJuSC-eg)
- [CCH2 georeferencing protocols and guides](https://www.capturingcaliforniasflowers.org/georeferencing-protocols-and-guides.html)
- [GLOBAL georeferencing protocols and guides](https://globaltcn.utk.edu/georeferencing)

## Imaging
When resources allow, image capture can be beneficial for mutiple reasons. First, ...

2D images (e.g., photographs) can be displayed directly in a Symbiota portal, whereas 3D imagery (e.g., surface scans) should be maintained in an external repository/database, such as [MorphoSource](https://www.morphosource.org). In the latter case, links can then be created between your specimen records in Symbiota and the external respository using Symbiota's [resource linking tools]([https://biokic.github.io/symbiota-docs/coll_manager/upload/links/](https://biokic.github.io/symbiota-docs/editor/links/#linking-associations). 

If your organization requires image hosting...

### Imaging 

# Example workflows

<iframe src="https://docs.google.com/presentation/d/1_b6990eETxSRmIVEb8eamaAhEuK3jWLxTB41YYcX_so/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

{: .notice--primary }
📬 **Questions?** Data providers are encouraged to contact paleoinformatics@gmail.com for assistance with questions related to developing a digitization workflow for fossil collections using Symbiota. Include “Symbiota” in the subject of your email, e.g. “Help with developing a workflow for my fossil collection using Symbiota”.


{% include related_list topics='symbiota' %}
{% include resource_list topics='symbiota' %}
{% include resource_card filename='krimmel-2022-workflows.yml' %}
