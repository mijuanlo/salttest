instala_itaca:
  cmd.run:
    - name: dpkg-query -W -f '${Status}' itaca 2>/dev/null | egrep -q '^install ok' || epic -u install itaca.epi

