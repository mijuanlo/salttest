#!/usr/bin/env python

import subprocess

def main():
    return {'uptime':subprocess.check_output('uptime')}