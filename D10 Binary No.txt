#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a=bin(n)
    m=c=0
    for i in a:
        if i=='1':
            c=c+1
        else:
            m=max(c,m)
            c=0
    print(max(c,m))