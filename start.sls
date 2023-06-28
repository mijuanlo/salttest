{% if data and 'id' in data %}
highstate_run:
  local.state.highstate:
    - tgt: {{ data['id'] }}
    - ret: highstate
{% endif %}
