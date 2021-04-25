#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'compressWord' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. INTEGER k

def letters(curr):
    # check if all letters in this substring are same.
    og = curr[0]
    for j in range(len(curr)):
        if curr[j]!=og:
            return False
    return True
        
def calc(word,k):
    # check each substring of length k in the given word
        
    for i in range(0,len(word)):
        if i+k-1<len(word):
            curr = word[i:i+k]
            if letters(curr) == True:
                #if a substring with all same letters is found, we remove it from the original word and return the new word.
                new_word = word.replace(curr,'')
                f = True
                return new_word,f
    f = False
    return word,f
    
def compressWord(word, k):
    # Write your code here
    flag = True
    while flag == True:
        word,f = calc(word,k)
        flag = f
        
    result,f = calc(word,k)
        
    return result

if _name_ == '_main_':
