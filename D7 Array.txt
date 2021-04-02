#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    i=len(arr)
    for j in range(i-1,-1,-1):
        print(arr[j],end=" ")
