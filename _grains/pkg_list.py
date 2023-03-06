#!/usr/bin/env python

import subprocess
import os

def main():
    if os.path.exists('/usr/bin/dpkg-query'):
        pkgs = subprocess.check_output(['/usr/bin/dpkg-query','-W','-f',"${Package} ${Version}\n"]).decode().split('\n')
        packages = {}
        for pkg in pkgs:
            try:
                name, version, *other = pkg.split(' ')
            except:
                pass
            packages.setdefault(name, [version])
        return { 'packages' : packages }
