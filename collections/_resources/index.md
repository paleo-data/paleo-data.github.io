---
title: Resources
parent: Home
nav_order: 2
layout: single
---

<table>
  <tr>
    <th>Title</th>
    <th>Creators</th>
    <th>Description</th>
    <th>Link</th>
  </tr>
{% for item in site.data.resources %}
  {% assign row = item[1] %}
  <tr>
    <td><a href="{% link {{ row.path }} %}">{{ row.title }}</a></td>
    <td>{{ row.creators }}</td>
    <td>{{ row.description }}</td>
    <td><a href="{{ row.link }}">{{ row.link }}</a></td>
  </tr>
{% endfor %}
</table>
