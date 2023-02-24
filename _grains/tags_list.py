#!/usr/bin/env python

import os

def main():
    try:
        return {'tags':os.listdir('/etc/lliurex-auto-upgrade')}
    except Exception as e:
        return {'tags':[str(e)]}