---
title: Tags
parent: Home
nav_order: 6
classes: wide
sidebar:
  nav: tags
---

<ul>
{% for tag in site.tags %}
  <li><a href="{{ tag.url | relative_url }}">{{ tag.title }}</a></li>
{% endfor %}
</ul>