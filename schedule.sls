schedule:
  highstate:
    enabled: True
    function: state.highstate
    minutes: 20
#{{pillar.get('schedule_time')}}
