#!/bin/python3
import random, sys


def frequency(file, plain):

    """ (str,str) -> dict of (str:int)

    Arguments:
    file -- the path of the file
    plain -- the alphanumeric set that you want to count

    Return:
    the frequency of the letters (specified in the plain) in the file
    
    """
    freq = {occur:0 for occur in plain}
    file = open(file,"r")
    for line in file:
        for occur in line:
            if occur not in plain: continue
            freq[occur] += 1
    file.close()
    return freq

# The specified set of letters for counting 
plain = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = sys.argv[1]
print(file)
freq = frequency(file,plain)
freq = {x: n for x,n in sorted(freq.items(),key=lambda item: item[1])}
print(freq)
