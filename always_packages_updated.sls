update_all_packages:
  pkg.uptodate:
    - name: '*'

#
# Other methods without for ALL packages:
#
# update_all_packages:
#   pkg.upgrade:
#     - refresh: True
