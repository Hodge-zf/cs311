#!/usr/bin/python3

import sys
import csv

if len(sys.argv) != 3:
    sys.stderr.write("Incorect number of command line arguments, exiting...\n")
    sys.exit()
value_count = {}
fields_list = int(sys.argv[1])
print(fields_list)

with open(sys.argv[2]) as infile:
    field_array = csv.reader(infile, delimiter=',')
    next(field_array)
    for row in field_array:
        i = 0
        while i < len(row):
            if i < fields_list:
                temp = row[i]
                value_count[temp] = value_count.get(temp, 0) + 1
                i += 1
            else:
                i = len(row)
    print(sorted(value_count.items(), key=lambda x: x[1], reverse=True))


