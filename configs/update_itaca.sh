#!/bin/bash
if [ "x$(apt-cache policy itaca|head -3|tail -2|cut -d':' -f2|uniq|wc -l)" == "x2" ]; then
	epic -u install itaca.epi
fi
