---
title: Paleo Data Knowledge Hub
layout: splash
header:
  overlay_image: /assets/images/header.jpg
  caption: "Photo credit: [NMNH](https://naturalhistory.si.edu/)"
  #actions:
  #  - label: "More Info"
  #    url: "/about"
excerpt: A community-curated resource for learning about capturing, managing, sharing, and discovering fossil data
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
      url: /data-ecosystem
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
This website is a hub designed to enable open access to information for anyone producing, managing, or utilizing paleontological specimen data. Ideally, the hub facilitates ongoing engagement and continuous knowledge sharing across stakeholder communities, in particular by hosting resources that are broadly relevant, and even adaptable to domains beyond paleo. All community users (e.g., you) are invited to engage as both information seekers and knowledge contributors. In the initial implementation of this knowledge hub (ongoing throughout 2025), content creation will focus deeply on the information needs of paleo collections professionals, and intro-level on the needs of paleo researchers using collections-based data.

{% capture now %}{{ "now" | date: "%Y-%m-%d" }}{% endcapture %}
{% assign upcoming = "" | split: "" %}
{% assign items = site.data["pdwg-happy-hours"] | sort: "date" %}
{% for item in items %}
  {% capture then %}{{ item.date | date: "%Y-%m-%d" }}{% endcapture %}
  {% if then >= now %}
    {% assign item_ = item.date | append: ": " | append: item.title | split: "|" %}
    {% assign upcoming = upcoming | concat: item_ %}
  {% endif %}
{% endfor %}

{% assign size = upcoming | size %}
{% if size > 0 %}
  <div class="notice--info upcoming">
    <strong>Upcoming "Happy Hour" meetings</strong>
    <ul>
    {% assign idx = 0 %}
    {% for item in upcoming %}
      <li{% if idx > 2 %} class="hidden"{% endif %} data-date="{{ item | slice: 0, 10}}">{{ item }}</li>
      {% assign idx = idx | plus: 1 %}
    {% endfor %}
    </ul>
    <p>Happy hours are biweekly meetings of the Paleo Data Working Group that take place every other Thursday at 12 PM Eastern Time. Please see the <a href="{{ '/community/pdwg-happy-hours' | relative_url }}">happy hour page</a> for details about how to attend.</p>
  </div>
{% endif %}

{% include feature_row %}
