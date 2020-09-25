#!/usr/bin/env python3

import re
import operator
import os

path = os.getcwd()
target_file=os.path.join(path, "syslog.log")
error_msg = {}
user_stat = {}

with open(target_file) as f:
    for line in f:
        if "ERROR" not in line:
            continue
        print(line.strip())
