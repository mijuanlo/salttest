#!/usr/bin/env python

import subprocess

def main():
    version = subprocess.check_output(['/usr/bin/dpkg-query','-W','-f',"${Version}", 'lliurex-version-timestamp']).decode()
    if isinstance(version,(list,dict)):
        version = str(version)
    return str(version) 

