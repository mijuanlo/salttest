import subprocess
import os.path
import os
import pwd

def desktop_present(name, user='all'):
    ret = {"name": name, "result": False, "comment": "", "changes": {}}
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
            for us in os.listdir('/home'):
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
        ret['result'] = True
    except Exception as e:
        out = str(e)
        ret['result'] = False
    if ret['result'] == True:
        ret['comment'] = 'Created for user/s: {}'.format(','.join(created))
    else:
        ret['comment'] = 'Created for user/s: {}\nNote: {}'.format(','.join(created),out)
    ret['changes'] = {"result": ret['comment']}
    return ret
