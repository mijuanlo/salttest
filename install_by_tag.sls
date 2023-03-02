{% for gra in grains['tags'] %}
{% for pkg in pillar.get('pkgs_'+gra) %}
{{ pkg }}:
  pkg.installed
{% endfor %}
{% endfor %}