#!/usr/bin/python3

import sys
import csv

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
    print(value_count)


