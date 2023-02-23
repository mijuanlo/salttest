sleep 2:
  cmd.run:
    - name: sleep 3

refresco_pillar:
  module.run:
    - name: saltutil.sync_all
    - refresh: True
