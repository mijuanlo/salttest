touch /tmp/kaka:
  cmd.run

{% for gra in grains['tags'] %}
{% if gra == 'jaja' %}
touch /tmp/kaka2:
  cmd.run
{% endif %}
{% endfor %}