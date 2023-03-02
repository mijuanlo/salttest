touch /tmp/kaka:
  cmd.run

{% for gra in grains['tags'] %}
{% for pkg in pillar.get('pkgs_'+gra) %}
touch /tmp/{{ pkg }}:
  cmd.run
{% endfor %}
{% endfor %}