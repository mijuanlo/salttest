import subprocess

def add_desktop(name, user='all'):
    ret = {"name": name, "result": False, "comment": "", "changes": {}}
    out = subprocess.check_output("cp /usr/share/applications/org.kde.kwrite.desktop /home/lliurex/Escriptori/",shell=True)
    ret['comment'] = out
    ret['result'] = True
    ret['changes'] = {"result": out}
    return ret
