---
layout: default
title: "Projects"
---

# Projects

{% if site.data.projects.projects %}
  {% for project_type in site.data.projects.projects %}
  ## {{ project_type.type }}
  {% for item in project_type.items %}
  - **[{{ item.name }}]({{ item.link }})**: {{ item.description }}
  {% endfor %}
  {% endfor %}
{% else %}
  No projects available at this time.
{% endif %}
