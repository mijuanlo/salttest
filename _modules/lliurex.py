import subprocess

def add_desktop(name, user='all'):
    return subprocess.check_output("cp /usr/share/applications/org.kde.kwrite.desktop /home/lliurex/Escriptori/",shell=True)