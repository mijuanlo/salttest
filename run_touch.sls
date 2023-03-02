touch /tmp/kaka:
  cmd.run

{% for gra in grains['tags'] %}
{% if gra == 'ja'+'ja' %}
touch /tmp/{% pillar.get('pkgs_jaja') %}:
  cmd.run
{% endif %}
{% endfor %}