---
title: Tags
parent: Home
nav_order: 3
classes: wide
sidebar:
  nav: tags
---

<ul>
{% for tag in site.tags %}
  <li><a href="{{ tag.url }}">{{ tag.title }}</a></li>
{% endfor %}
</ul>