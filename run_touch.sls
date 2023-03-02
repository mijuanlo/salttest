touch /tmp/kaka:
  cmd.run

{% if grains['tags'] == 'jaja' %}
touch /tmp/kaka2:
  cmd.run
{% endif %}