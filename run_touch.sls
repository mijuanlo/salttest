touch /tmp/kaka:
  cmd.run

touch /tmp/{% grains['tags'] %}:
  cmd.run