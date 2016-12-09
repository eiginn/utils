#!/usr/bin/env python2
"""
usage:
    mac_conv.py 54AB3A7AE999
    mac_conv.py unix_expanded 54AB3A7AE999
    echo -e '54AB3A7AE999\\n54AB3A7AE998' | mac_conv.py unix_expanded
"""

import sys
from netaddr import EUI, mac_bare, mac_cisco, mac_eui48
from netaddr import mac_pgsql, mac_unix, mac_unix_expanded

type_map = {
    'bare': mac_bare,
    'cisco': mac_cisco,
    'eui64': mac_eui48,
    'pgsql': mac_pgsql,
    'unix': mac_unix,
    'unix_expanded': mac_unix_expanded
    }

if len(sys.argv) < 2 or sys.argv[-1] == '-h':
    print __doc__
    sys.exit(0)

if sys.stdin.isatty():
    try:
        m = EUI(sys.argv[-1])
    except:
        print "Doesn't look like a mac address"
        sys.exit(1)
    if len(sys.argv) > 2:
        m._set_dialect(type_map[sys.argv[1]])
        print m
    else:
        for dia in (mac_bare, mac_cisco, mac_eui48,
                    mac_pgsql, mac_unix, mac_unix_expanded):
            print dia.__doc__
            m._set_dialect(dia)
            print m
        sys.exit(0)
else:
    data = sys.stdin.read().splitlines()
    for mac in data:
        m = EUI(mac)
        m._set_dialect(type_map[sys.argv[1]])
        print m
