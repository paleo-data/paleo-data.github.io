---
title: Resources
parent: Home
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
    <td>{{ row.title }}</td>
    <td>{{ row.creators }}</td>
    <td>{{ row.description }}</td>
    <td>{{ row.link }}</td>
  </tr>
{% endfor %}
</table>
