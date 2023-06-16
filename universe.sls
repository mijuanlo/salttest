#sleep 2:
#  cmd.run:
#    - name: sleep 3

refresco_pillar:
  module.run:
    - name: saltutil.sync_all
    - refresh: True

# test with: 
#  -> salt-call schedule.show_next_fire_time highstate
#  -> salt-call schedule.list show_all=True
#  -> salt-call pillar.data
#  -> salt-call pillar.items
#  -> salt-call state.show_sls universe
#  -> salt-call slsutil.renderer salt://universe.sls
#  -> salt '*' slsutil.renderer salt://universe.sls


highstate:
  schedule.present:
    - function: state.highstate
    - minutes: {{ pillar.get('schedule_time',60) }}
#    - splay: 600

# more help:
# salt-run fileserver.file_list
# 