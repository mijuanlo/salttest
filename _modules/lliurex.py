#
# Example proof-of-concept minimal module for copy desktop app to any home
#
import subprocess
import os
import pwd

#
#def add_desktop(name, user='all'):
#    return subprocess.check_output("cp /usr/share/applications/org.kde.kwrite.desktop /home/lliurex/Escriptori/",shell=True)

def add_desktop(name, user='all'):
    created = []
    try:
        filename='/usr/share/applications/'+name
        if not os.path.isfile(filename):
            raise Exception('File {} not available'.format(filename))
        if user != 'all':
            dirname=subprocess.check_output("su {} - -c 'xdg-user-dir DESKTOP'".format(user),shell=True,stderr=subprocess.STDOUT)
            try:
                dirname=dirname.decode()
            except:
                pass
            dirname=dirname.strip()
            if not dirname or not os.path.isdir(dirname):
                raise Exception('usererror: user {} with desktop {} not available'.format(user,dirname))
            outmsg = subprocess.check_output("cp {} {}".format(filename,dirname),shell=True,stderr=subprocess.STDOUT)
            created.append(user)
        else:
            out = []
            for us in (x.pw_name for x in pwd.getpwall()):
                dirname=subprocess.check_output("su {} - -c 'xdg-user-dir DESKTOP' -s /bin/sh".format(us),shell=True,stderr=subprocess.STDOUT)
                try:
                    dirname=dirname.decode()
                except:
                    pass
                dirname=dirname.strip()
                if not dirname or not os.path.isdir(dirname):
                    continue
                outmsg = subprocess.check_output("cp {} {}".format(filename,dirname),shell=True,stderr=subprocess.STDOUT)
                created.append(us)
                if outmsg:
                    out.append(outmsg)
            if out:
                out = ','.join(out)
        return True
    except Exception as e:
        return False