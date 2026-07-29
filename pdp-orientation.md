---
title: Test
description: The test page includes widgets and other elements that have been customized for the Paleo Data Knowledge Hub.
status: draft
nav_order: 1
sidebar:
  nav: [sidebar]
  collapsible: true
  expanded: [community]
contributors: ["Adam Mansur"]
topics: [invalid]
last_modified_at: 2025-10-01
---

# Introduction
Thank you for your interest in using the {% include resource_link filename='pdp.yml' %}, a Symbiota-based data portal for managing and publishing fossil specimen data. This documentation is intended to help data providers 1) determine whether this resource will be an appropriate tool for managing and sharing data associated with their collection and 2) understand key information for leveraging the portal’s built-in tools for data mobilization.

# Portal Scope
The Paleo Data Portal’s scope is described on the home page, [https://paleo.symbiota.org](paleo.symbiota.org). The portal is intended for managing and sharing specimen data from fossil collections that can be used for research and are held in public trust, for example, by a university collection or nonprofit museum. The portal’s scope is limited to extinct organisms and their traces (i.e., fossils) and collections that intend to use the portal for active data management. The Paleo Data Portal is not intended for use by teaching collections, collections that are not publicly accessible, geological samples that do not contain fossils, archaeological or anthropological materials, or neontological (extant) specimen data.






This a resource with a tooltip: {% include resource_link filename='bauer-et-al-2022.yml' %}. It should display as a link to an external resource with a tooltip that appears on hover. Tooltips displayed using this widget are based on the annotation field. If that field contains any formatting code, it may break the tooltip. The first appearance of the word tooltip should be underlined and include a tooltip but no link.

This paragraph includes a term defined manually in the glossaries/custom.yml file, {% include glossary term="Internationalized Resource Identifier" namespace="" %}.

This is a paragraph including {% include glossary term="Darwin Core" namespace="" %} terms, like {% include glossary term="geodeticDatum" namespace="dwc" %} and {% include glossary term="maximumDistanceAboveSurfaceInMeters" namespace="dwc" %}. Those terms should display as links to the Darwin Core Quick Reference Guide and should show a definition on hover. Only the first appearance of a term on each page should include the tooltip, so geodeticDatum in this sentence should appear as plain text. Note that terms do not use a widget or any other syntax. The script that builds the page identifies them automatically.

Here are some items that should not include tooltips:

- # dwc:institutionID
- [dwc:collectionID](#link)
- <a href="#top">dwc:datasetID</a>

But these should: 

- {% include glossary term="institutionID" namespace="dwc" %}
- {% include glossary term="collectionID" namespace="dwc" %}
- {% include glossary term="datasetID" namespace="dwc" %}

## Notices

{: .notice}
Created with `{: .notice}`

{: .notice--info}
Created with `{: .notice--info}`

{: .notice--warning}
Created with `{: .notice--warning}`

{: .notice--danger}
Created with `{: .notice--danger}`

{: .notice--tip}
Created with `{: .notice--tip}`

{% include resource_list topics='symbiota' %}

{% include resource_list topics='geography|georeference' %}

{% include resource_list topics='geography|georeference|data wrangling' %}

## Embedded content

<iframe src="https://docs.google.com/presentation/d/1yJFsaCnBC28zW8UtLfl3tnJayk3w-BRDtVzyZYpD1TI/embed?start=false&loop=false&delayms=10000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


<iframe width="480" height="299" src="https://www.youtube.com/embed/MfXTtQ2A5hY?si=L5TZHf-BohPXUk52" title="test video from YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
