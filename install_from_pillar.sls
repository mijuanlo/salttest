{% for package in pillar.get('pkgs') %}
{{package}}:
pkg.installed
{% endfor %}
