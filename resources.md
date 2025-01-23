---
title: Resources
parent: Home
nav_order: 2
classes: wide
sidebar:
  nav: resources
---

<table>
  <tr>
    <th>Title</th>
    <th>URL</th>
  </tr>
{% for resource in site.resources %}
  <tr>
    <td><a href="{{ resource.url }}">{{ resource.title }}</a></td>
    <td><a href="{{ resource.resource_url }}">{{ resource.resource_url }}</a></td>
  </tr>
{% endfor %}
</table>
