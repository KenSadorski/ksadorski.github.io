---
layout: default
title: "Certifications and Badges"
---

# Certifications and Badges

{% for cert in site.data.certifications.certifications %}
  - **[{{ cert.name }}]({{ cert.url }})**
    - *{{ cert.organization }}*, {{ cert.year }}
{% endfor %}
