/etc/apt/sources.list:
  file.managed:
    - source: salt://configs/sources.list
    - skip_verify: True


