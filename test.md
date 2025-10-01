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

This page is used to test widgets and other features.

This a resource with a tooltip: {% include resource_link filename='bauer-et-al-2022.yml' %}. It should display as a link to an external resource with a tooltip that appears on hover. Tooltips displayed using this widget are based on the annotation field. If that field contains any formatting code, it may break the tooltip. The first appearance of the word tooltip should be underlined and include a tooltip but no link.

This paragraph includes a term defined manually in the glossaries/custom.yml file, Internationalized Resource Identifier.

This is a paragraph including Darwin Core terms, like dwc:geodeticDatum and dwc:maximumDistanceAboveSurfaceInMeters. Those terms should display as links to the Darwin Core Quick Reference Guide and should show a definition on hover. Only the first appearance of a term on each page should include the tooltip, so geodeticDatum in this sentence should appear as plain text. Note that terms do not use a widget or any other syntax. The script that builds the page identifies them automatically.

Here are some items that should not include tooltips:

- # dwc:institutionID
- [dwc:collectionID](#link)
- <a href="#top">dwc:datasetID</a>

But these should: 

- dwc:institutionID
- dwc:collectionID
- dwc:datasetID

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
