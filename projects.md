---
layout: default
title: "Projects"
---

# Projects

{% if site.data.projects %}
  - **Status:** {{ site.data.projects[0].status | capitalize }}
  - {{ site.data.projects[1].message }}
{% endif %}
