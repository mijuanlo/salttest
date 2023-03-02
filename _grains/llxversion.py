#!/usr/bin/env python

import subprocess

def main():
    version = subprocess.check_output(['/usr/bin/dpkg-query','-W','-f',"${Version}", 'lliurex-version-timestamp']).decode().split('\n')
    if version:
        return { 'llxversion' : str(version) }

