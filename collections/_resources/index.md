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
    <td><a href="/resources{{ row.url | relative_url }}">{{ row.title }}</a></td>
    <td>{{ row.creators }}</td>
    <td>{{ row.description }}</td>
    <td><a href="{{ row.link }}">{{ row.link }}</a></td>
  </tr>
{% endfor %}
</table>
