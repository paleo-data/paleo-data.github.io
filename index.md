---
title: Paleo Data Knowledge Hub
layout: splash
header:
  overlay_image: /assets/images/header.jpg
  caption: "Photo credit: [NMNH](https://naturalhistory.si.edu/)"
  #actions:
  #  - label: "More Info"
  #    url: "/about"
excerpt: Lorem ipsum dolor sit amet, consectetur adipiscing elit
feature_row:
    - image_path: /assets/images/ri--community-line.png
      alt: "A globe icon"
      title: "Community"
      excerpt: 
      url: /community
    - image_path: /assets/images/ri--node-tree.png
      alt: "A globe icon"
      title: "Data Ecosystem"
      excerpt: 
      url: /data_ecosystem
    - image_path: /assets/images/ri--info-card-line.png
      alt: "A globe icon"
      title: "Topics"
      excerpt: 
      url: /topics
    - image_path: /assets/images/ri--questionnaire-line.png
      alt: "A globe icon"
      title: "Explanations"
      excerpt: 
      url: /explanations
    - image_path: /assets/images/ri--book-shelf-line.png
      alt: "A globe icon"
      title: "How To Guides"
      excerpt: 
      url: /how_to_guides
    - image_path: /assets/images/ri--treasure-map-line.png
      alt: "A globe icon"
      title: "Tutorials"
      excerpt: 
      url: /tutorials
---

Welcome to the Paleo Data Hub!

{% capture now %}{{ "now" | date: "%s" }}{% endcapture %}
{% assign upcoming = "" | split: "" %}
{% assign items = site.data.pdwg_happy_hours | sort: "date" %}
{% for item in items %}
  {% capture then %}{{ item.date | date: "%s" }}{% endcapture %}
  {% if then >= now %}
    {% assign item_ = item.date | append: ": " | append: item.title | split: "|" %}
    {% assign upcoming = upcoming | concat: item_ %}
  {% endif %}
{% endfor %}

{% assign size = upcoming | size %}
{% if size > 0 %}
  <div class="notice--info upcoming">
    <strong>Upcoming Paleo Data Happy Hours</strong>
    <ul>
    {% assign idx = 0 %}
    {% for item in upcoming %}
      <li{% if idx > 2 %} class="hidden"{% endif %} data-date="{{ item | slice: 0, 10}}">{{ item }}</li>
      {% assign idx = idx | plus: 1 %}
    {% endfor %}
    </ul>
    <p>Happy hours take place every other Thursday at 12 PM ET. Please see the 
    <a href="{{ '/community/pdwg-happy-hours' | relative_url }}">happy hour page</a> for details about how to attend.</p>
  </div>
{% endif %}

{% include feature_row %}
