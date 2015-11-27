#!/usr/bin/python
# Filename: finally.py

import time

try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line,end='')
finally:
    f.close()
    print('Cleaning up...closed the file')