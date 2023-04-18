import subprocess

def desktop_present(name, user='all'):
    ret = {"name": name, "result": False, "comment": "", "changes": {}}
    try:
        out = subprocess.check_output("cp /usr/share/applications/org.kde.kwrite.desktop /home/lliurex/Escriptori/",shell=True,stderr=subprocess.STDOUT)
        ret['result'] = True
    except Exception as e:
        out = str(e)
        ret['result'] = False
    ret['comment'] = name
    ret['changes'] = {"result": out}
    return ret
