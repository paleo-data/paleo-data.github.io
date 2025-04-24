---
title: Prepare your data for import into Symbiota
last_modified_at: 2025-04-23
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
topics: [symbiota, data wrangling]
---

{: .notice--info }
This guide is intended to complement documentation for [getting started in the Symbiota Paleo Data Portal](/knowledge-hub/how-to-guides/how-to-get-started-in-the-symbiota-paleo-data-portal.html), as well as the official Symbiota user documentation, [Symbiota Docs](https://biokic.github.io/symbiota-docs/). Symbiota Docs provides general guidance for working in Symbiota-based data portals and should be referenced for basic functions and workflows. This manual expands on this resource to provide discipline-specific information for fossil collections.

This document outlines actions you can take to prepare any existing digital catalog records from your fossil collection for ingestion into Symbiota. These steps can help make your data more easily managed and discovered, and are therefore _highly_ recommended.

## Formatting data for import

### Steps you can take to ready your records for ingestion
1. Familiarize yourself with the [Darwin Core data standard](https://dwc.tdwg.org/terms/), which is the basis for the majority of [Symbiota’s Data Fields](https://biokic.github.io/symbiota-docs/editor/edit/fields/).
2. If you maintain existing catalog records to be imported into Symbiota, perform some data cleaning to align your records to the Symbiota data fields and formatting specified in the previous step. [OpenRefine](https://doi.org/10.5281/zenodo.6574728) is free software that can be used for this purpose. **Highly recommended: Use the checklist below to prepare your data for import.**
3. If you’d like a template to follow, [this spreadsheet](https://docs.google.com/spreadsheets/d/1b1aN6NuoOEN4IlToV3Uk33xpSwrbcn3-uceSnlgf8JI/edit?usp=sharing) is preformatted for use with Symbiota. Not all fields are required to contain data. Your spreadsheet must be converted to CSV format prior to ingestion into the portal, which can be easily accomplished in a program like [Microsoft Excel](https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6) or [Google Sheets](https://support.google.com/docs/answer/49114?sjid=17532513690429081890-NC).

#### Data formatting checklist
If you maintain cataloged specimen records in a spreadsheet, this information can be imported into Symbiota in CSV format. Before doing so, it is highly recommended that you use this checklist to prepare your data for ingestion to maximize the interoperability between your data and that of other collections, ultimately making your records more discoverable and useful for research. Additional data cleaning can be performed once your records are in Symbiota. The checklist below has been compiled based on scenarios observed in other datasets from fossil collections prepared for import. The [Symbiota Data Import Fields](https://biokic.github.io/symbiota-docs/coll_manager/upload/fields/) guide provides important information about fields available in Symbiota, as well as the types of data that can be imported into each one—for instance, which fields can only contain numbers, dates only, textual data, etc.—and how this information should be formatted. ~Examples of datasets that have been cleaned in preparation for ingestion into Symbiota can be found [here]()~. 

| Dataset | After Cleaning |
| --------------- | ------ |
| ASU Paleobotany | [link] | 
| PH Paleobotany  | [link] |











# Introduction
## What is Symbiota?
 <img style="float: left; margin: 0px 15px 0px 0px;" width="25%" src="/knowledge-hub/assets/images/symbiota_logo-lg.png" alt="Symbiota Logo" caption="Symbiota Logo">
[Symbiota](https://github.com/Symbiota/Symbiota) is open source software guided by the [Darwin Core](http://dwc.tdwg.org/terms) data standard for creating themed data portals to help people share and manage biodiversity data. The PDP utilizes the version of Symbiota code that is developed by the [Symbiota Support Hub](https://paleo.symbiota.org/portal/misc/contacts.php](https://symbiota.org/about-us)) (SSH), a University of Kansas-based team dedicated to the technical and social implementation of Symbiota-based data portals. The SSH provides technical support for PDP users—like nightly portal backups and routine code upgrades—whereas the portal's [Steering Committee](https://paleo.symbiota.org/portal/misc/contacts.php) provides guidance on best practices related to the management of fossil specimen data.

## What is the "Paleo Data Portal"?
The Paleo Data Portal is a Symbiota-based data portal hosted by the Symbiota Support Hub that exists to:
- Provide **low barrier-to-entry** data mobilization platform
- Increase **data accessibility** for research use
- **Build community** with and among fossil collections not previously engaged in digitization efforts
- **Integrate with [PDWG](https://paleo-data.github.io/about)’s efforts** to develop best practices in paleo data management and publishing
- Provide a **testing ground** for technical solutions, e.g. those related to taxonomy

## How to participate?
If you manage a fossil collection and would like to use this portal to manage your specimen data, first carefully review the portal's [community guidelines](https://paleo.symbiota.org/portal/includes/usagepolicy.php). If the portal seems suitable for your needs after reviewing the guidlines, please complete [this form](https://forms.gle/VGH9Rqg4ujpNcj1C8). Be aware that this data portal is only inteded for use by collections that are maintained in a publicly accessible and permanent repositories. 

{: .notice--info }
📃 Prospective data providers may wish to reference the complete directory of [Symbiota portals](https://symbiota.org/symbiota-portals).

# Getting started
## Data preparation
‼️ If you maintain existing digital catalog records in a spreadsheet, this information can be imported into the Paleo Data Portal. Data providers are strongly advised to refer to the guide, [_How to prepare your data for import into Symbiota_](), prior to ingesting new data in the portal. 

## Essential functions
This section of the guide will provides an introduction to the portal's essential functions for data providers.
<iframe src="https://docs.google.com/presentation/d/1KTuhJWM_dSGWAahTZhDVspilIthPrsy36JlVFDWDlG0/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

{% include resource_card filename='pearson-2022.yml' %}

{: .notice--info }
The Paleo Data Portal is made possible by the US National Science Foundation (NSF Award#[2324690
](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2324690)/[2525603](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2525603)).

{% include related_list topics='symbiota' %}

{% include resource_list topics='symbiota' %}
