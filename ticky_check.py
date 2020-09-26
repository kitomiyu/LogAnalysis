#!/usr/bin/env python3

import re
import operator
import os
import csv

path = os.getcwd()
target_file=os.path.join(path, "syslog.log")

error_msg = {}
user_stat = {}

user_name_pattern = r"\(([\w*.]*)\)"
error_msg_pattern = r"[INFO|ERROR] ([\w ]*)"

with open(target_file) as f:
    for line in f:
        result_usern = re.search(user_name_pattern, line)

        if result_usern[1] not in user_stat.keys():
            user_stat[result_usern[1]] = {}
            user_stat[result_usern[1]]["INFO"] = 0
            user_stat[result_usern[1]]["ERROR"] = 0
        if "ERROR" in line:
            # error msg (error, count)
            result_error = re.search(error_msg_pattern, line)
            error_msg[result_error[1]] = error_msg.get(result_error[1], 0) + 1
            user_stat[result_usern[1]]["ERROR"] += 1
        if "INFO" in line:
            user_stat[result_usern[1]]["INFO"] += 1

error_msg = sorted(error_msg.items(), key=operator.itemgetter(1), reverse=True)
user_stat = sorted(user_stat.items())

# generate two report file error_message.csv and user_statistics.csv.
with open("error_message.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["ERROR", "COUNT"])
    for row in error_msg:
        writer.writerow(row)

with open("user_statistics.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["USERNAME", "INFO", "ERROR"])
    for row in user_stat:
        user, log_type = row
        line = [user, log_type["INFO"], log_type["ERROR"]]
        writer.writerow(line)
