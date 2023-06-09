update_all_packages:
  module.run:
    - name: pkg.upgrade
    - dist_upgrade: True
    - refresh: True
    

#    - require:
#      - module: update_packages
#
# Other methods without for ALL packages:
#
# update_all_packages:
#   pkg.upgrade:
#     - refresh: True
