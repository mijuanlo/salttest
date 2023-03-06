# use command with "salt script default" or from salt command line with "salt '*' state.apply force_register"
force_register:
  cmd.run:
    - name: mv /etc/salt/minion /tmp/
