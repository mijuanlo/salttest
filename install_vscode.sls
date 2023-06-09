instala_vscode:
  cmd.run:
    - name: dpkg-query -W -f '${Status}' code 2>/dev/null | egrep -q '^install ok' || epic -u install zero-fp-informatica.epi code

