# EECE2540 Python and Wireshark Assignment 
# Tracy Qiu NUID: 001313852 10/29/21

import csv

with open('EECE2540_001313852_PyWS.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(bytearray.fromhex(row["Data"]).decode())