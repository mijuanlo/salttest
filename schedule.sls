schedule:
  highstate:
    enabled: True
    function: state.highstate
    minutes: {{pillar.get('schedule_time')}}
