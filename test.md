---
title: Test
status: draft
nav_order: 1
sidebar:
  nav: [sidebar]
  collapsible: true
  expanded: [community]
---

This page is used to test widgets and other features.

This a resource with a tooltip: {% include resource_link filename='bauer-et-al-2022.yml' %}. It should display as a link to an external resource with a tooltip that appears on hover. Tooltips displayed using this widget are based on the annotation field. If that field contains any formatting code, it may break the tooltip. The first appearance of the word tooltip should be underlined and include a tooltip but no link.

This is a paragraph including Darwin Core terms, like geodeticDatum and maximumDistanceAboveSurfaceInMeters. Those terms should display as links to the Darwin Core Quick Reference Guide and should show a definition on hover. Only the first appearance of a term on each page should include the tooltip, so geodeticDatum in this sentence should appear as plain text. Note that terms do not use a widget or any other syntax. The script that builds the page identifies them automatically. 