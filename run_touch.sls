touch /tmp/kaka:
  cmd.run

{% for gra in grains['tags'] %}
{% if gra == 'ja'+'ja' %}
{% for pkg in pillar.get('pkgs_'+gra) %}
touch /tmp/{{ pkg }}:
  cmd.run
{% endfor %}
{% endif %}
{% endfor %}