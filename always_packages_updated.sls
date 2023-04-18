update_all_packages:
  pkg.uptodate:
    - name: '*'
    - refresh: True
    - require:
      - module: update_packages
#
# Other methods without for ALL packages:
#
# update_all_packages:
#   pkg.upgrade:
#     - refresh: True
