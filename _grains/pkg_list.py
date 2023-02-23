#!/usr/bin/env python

import subprocess

def main():
    pkgs = subprocess.check_output(['/usr/bin/dpkg-query','-W','-f',"${Package} ${Version}\n"]).decode().split('\n')
    packages = {}
    for pkg in pkgs:
        try:
            name, version, *other = pkg.split(' ')
        except:
            pass
        packages.setdefault(name, [version])
    return { 'packages' : packages }

