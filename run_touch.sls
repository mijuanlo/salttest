touch /tmp/kaka:
  cmd.run

{% for gra in grains['tags'] %}
{% if gra == 'ja'+'sja' %}
touch /tmp/kaka2:
  cmd.run
{% endif %}
{% endfor %}