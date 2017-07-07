#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:42:39 2017

This is a test set on math and string

@author: guochendai
"""

#--------------------------------------------------------maths

#Reverse Integer: Reverse digits of an integer.
#Example1: x = 123, return 321. Example: x = -123, return -321.

def reverseint(x):
    if x==0:
        return x
    if x<0:
        tmp = -1*x
        r = -1
    else:
        tmp=x
        r=1
    ret=0
    
    while tmp!= 0:
        ret = 10*ret +tmp%10
        tmp = tmp/10
    return r*ret

print reverseint(-23497)


#-------------------------------------------------------- string



