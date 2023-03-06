#!/usr/bin/env python

import os

def main():
    if os.path.exists('/etc/lliurex-auto-upgrade/tags'):
        try:
            return {'tags':os.listdir('/etc/lliurex-auto-upgrade/tags')}
        except Exception as e:
            return {'tags':[str(e)]}