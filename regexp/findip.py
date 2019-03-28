#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import re

IP_FILE = r'ipv4v6.txt'

pv4 = re.compile(r'\d{1,3}(\.\d{1,3}){3}')
pv6 = re.compile(r'[\da-f]{0,4}(:[\da-f]{0,4}){3,7}')
pv6_dual = re.compile(r'[\da-f]{0,4}(:[\da-f]{0,4}){1,3}(\.\d{1,3}){3}')

with open(IP_FILE) as f:
    for ip in f:
        ip = ip.strip()

        matched = False

        # IPv4
        if pv4.fullmatch(ip):
            matched = True

            # Validation
            parts = ip.split('.')
            for part in parts:

                octet = int(part)
                matched = matched and octet >= 0 and octet < 256
        # IPv6, IPv6 dual
        elif pv6.fullmatch(ip) or pv6_dual.fullmatch(ip):
            matched = True

        # Print if any valid ip found
        if matched:
            print(ip)