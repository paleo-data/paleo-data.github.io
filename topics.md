---
title: Browse by topic
description: Use the list to facet results and browse Knowledge Hub content by topics. Sort by frequency or alphabetical using the icons at the top of the list.
status: published
last_modified_at: 2025-09-17
nav_order: 2.5
layout: faceted
facet_data: indexed
facet_keys: [tags]
sidebar:
  nav: [sidebar]
  collapsible: true
---

<table class="faceted">
  <tr><th>Resource</th><th>Kind</th></tr>
  {% for item in site.data[page.facet_data] %}
    <tr data-tags="{{ item.tags | join: '|'}}">
      <td><a {% if item.kind == 'external' %}class="external" {% endif %}href="{% if item.kind == 'external' %}{{ item.url }}{% else %}{{ item.url | relative_url}}{% endif %}">{{ item.title }}</a></td>
      <td>{{ item.kind | capitalize | replace: "Pdwg", "PDWG" }}</td>
    </tr>
  {% endfor %}
</table>
