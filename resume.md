---
layout: default
title: "Resume"
---

# Resume

## Summary
{% for item in site.data.resume.summary %}
  - {{ item }}
{% endfor %}

## Experience
{% for job in site.data.resume.experience %}
  - **{{ job.title }}** at *{{ job.company }}* ({{ job.duration }})
    - {{ job.description }}
{% endfor %}

## Education
{% for edu in site.data.resume.education %}
  - {{ edu.degree }}, {{ edu.institution }} ({{ edu.year }})
{% endfor %}

## Skills
{% for skill in site.data.resume.skills %}
  - {{ skill }}
{% endfor %}
