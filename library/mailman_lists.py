#!/usr/bin/python2

import imp
import json
import sys

paths = imp.load_source('paths', '/usr/lib/mailman/bin/paths.py')

from Mailman.MailList import MailList
from Mailman.Utils import list_names

json.dump({
    'ansible_facts': {
        'mailman': {
            'lists': [MailList(name, lock=0).internal_name() for name in list_names()],
        },
    },
}, sys.stdout, indent=2)
