#!/usr/bin/env python

import subprocess
import os.path

def main():
    if os.path.exists('/usr/bin/dpkg-query'):
        version = subprocess.check_output(['/usr/bin/dpkg-query','-W','-f',"${Version}", 'lliurex-version-timestamp']).decode()
        if isinstance(version,(list,dict)):
            version = str(version)
        return {'lliurex-version':str(version)}

