---
title: Tags
parent: Home
layout: single
---

{% for item in site.data.tags %}
  {% assign tag = item[0] %}
  {% assign pages = item[1] %}
  <h2>{{ tag }}</h2>
  <ul>
    {% for page in pages %}
    <li><a href="{% link {{ page.path }} %}">{{ page.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

