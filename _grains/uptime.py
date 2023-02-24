#!/usr/bin/env python

import subprocess

def main():
    try:
        return {'uptime':subprocess.check_output('uptime').decode().split()[0]}
    except Exception as e:
        return {'uptime':str(e)}