#!/usr/bin/env python3

import re
import operator
import os

path = os.getcwd()
target_file=os.path.join(path, "syslog.log")

error_msg = {}
user_stat = {}

user_name_pattern = r"\(([\w*.]*)\)"
error_msg_pattern = r"[INFO|ERROR] ([\w ]*)"


with open(target_file) as f:
    for line in f:
        result_usern = re.search(user_name_pattern, line)
        if "ERROR" in line:
            # error msg (error, count)
            result_error = re.search(error_msg_pattern, line)
            error_msg[result_error[1]] = error_msg.get(result_error[1], 0) + 1
        # check user statistics (username, info, error)



print(sorted(error_msg.items(), key=operator.itemgetter(1), reverse=True))
