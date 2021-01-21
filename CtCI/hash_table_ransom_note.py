#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    count = 0
    for word in note:            
        if word in magazine:
            magazine.remove(word)
            count += 1
        else:
            break
    if count == len(note):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
