

import math
import os
import random
import re
import sys


def solve(s):
    finalWords = []
    words = s.split(" ")
    for i in words:

       finalWords.append(i.capitalize())
    ss = ' '.join(finalWords)
    return ss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
