#!/usr/bin/env python

import glob
import re

def main():
    filelist = glob.glob('/etc/apt/**/*.list',recursive=True)
    repos = {}
    for file in filelist:
        with open(file,'r') as fp:
            for line in fp.readlines():
                m = re.match(r'^deb\s+([[][^]]+[]])*(.*)$',line)
                if m:
                    groups = m.groups()
                    if len(groups) > 1:
                        groups = groups[1].split()
                        if len(groups) > 2:
                            repo = groups[0]
                            distro = groups[1]
                            components = groups[2:]
                            repos.setdefault(repo,{})
                            repos[repo].setdefault(distro,[])
                            for component in components:
                                if component not in repos[repo][distro]:
                                    repos[repo][distro].append(component)
    foreman_print = {}
    for repo in repos:
        line = []
        for distro in repos[repo]:
            line.append(distro)
            for component in repos[repo][distro]:
                line.append(component)
        foreman_print.setdefault(repo,' '.join(line))
    return { 'aptrepos' : foreman_print }
main()