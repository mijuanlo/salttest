touch /tmp/kaka:
  cmd.run

touch /tmp/{% pillar.get('pkgs'+'_jaja') %}:
  cmd.run