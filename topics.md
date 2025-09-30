---
title: Browse by topic
description: Use the list to facet results and browse Knowledge Hub content by topics. Sort by frequency or alphabetical using the icons at the top of the list, or read the topic definitions at [the bottom of the page](#topics).
status: published
last_modified_at: 2025-09-17
nav_order: 2.5
layout: faceted
facet_data: indexed
facet_keys: [tags, kind]
sidebar:
  nav: [sidebar]
  collapsible: true
---





<table class="faceted">
  <tr><th>Resource</th><th>Kind</th></tr>
  {% for item in site.data[page.facet_data] %}

    {% assign tags = '' %}
    {% for key in page.facet_keys %}
      {% capture tags_ %}|{{ item[key] | join: '|' }}{% endcapture %}
      {% capture tags %}{{ tags | append: tags_ }}{% endcapture %}
    {% endfor %}

    {% assign tags = tags | replace: '||', '|' | remove_first: '|' %}

    <tr data-tags="{{ tags }}">
      <td><a {% if item.kind == 'resource' %}class="external" {% endif %}href="{% if item.kind == 'resource' %}{{ item.url }}{% else %}{{ item.url | relative_url}}{% endif %}">{{ item.title }}</a></td>
      <td>{{ item.kind | capitalize | replace: 'Pdwg', 'PDWG' }}</td>
    </tr>
  {% endfor %}
</table>

<h2>Topics<a name="topics"></a></h2>
<dl>
{% for tag in site.data.topics %}
  {% assign slug = tag["topic"] | slugify %}
  {% capture url %}{{ '/topics?topic=' | append: slug }}{% endcapture %}
  <dt><a href="{{ url | relative_url }}">{{ tag['topic'] }}</a></dt>
  <dd>{{ tag['definition'] }}</dd>
{% endfor %}
</dl>


