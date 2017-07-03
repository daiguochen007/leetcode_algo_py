#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:17:36 2017

This is a test set on backtracking 回溯法，用DFS解决
combination组合数
permutation排列数

@author: guochendai
"""

############### combination
#--------------------------------- combination O(N!) 
# or will use k for to solve it
import itertools as it

def getcomb(n,k):
    return [c for c in it.combinations(range(1,n+1),k)]

print getcomb(5,2)

def combine(n,k):
    res = []
    if n<=0:
        return res
    DFS(res,[],n,k,1)
    return res

def DFS(res,curr,n,k,level):
    if len(curr)==k:
        res.append(curr[:]) #notice
        return
    if len(curr)>k:
        return
    for i in range(level,n+1):
        curr.append(i)
        DFS(res,curr,n,k,i+1)
        curr.pop()

print combine(5,2)

#--------------------------------- combination sum in sorted array O(N!)
def getcombsum(array,target):
    res = []  
    if target<0 or len(array)==0:
        return res
    backtracking(res,[],array,target,0)
    return res

def backtracking(res,curr,array,target,level):
    if target==0:
        res.append(curr[:])
        return
    if target<0:
        return
    for i in range(level,len(array)):
        target -= array[i]
        curr.append(array[i])
        backtracking(res,curr,array,target,i)     # change to i+1 can avoid repeat element
        curr.pop()
        target += array[i]
        
print getcombsum([4,6,9,2,3,5],8)

# ------------------------------letter combination of a phone number  O(3^n)
def getphonecomb(array):
    d={0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    res = []
    comb(res,[],array,d,0)
    return res

def comb(res,temp,array,d,level):
    if level == len(array):
        res.append("".join(temp[:]))
        return
    index = array[level]
    for i in range(len(d[index])):
        temp.append(d[index][i])
        comb(res,temp,array,d,level+1)
        temp.pop()
    return

print getphonecomb([2,3])

#--------------------------------- subsets
def subsets(array):
    res=[[]]
    for k in range(1,len(array)+1):
        res += [list(c) for c in it.combinations(array,k)]
    return res

print subsets([1,2,3])

def subsets2(array):
    res = [[]]
    if len(array)==0:
        return res
    generate(res,[],array,0)
    return res

def generate(res,curr,array,level):
    if level == len(array):
        return
    for i in range(level,len(array)):
        curr.append(array[i])
        res.append(curr[:])
        generate(res,curr,array,i+1)
        curr.pop()

print subsets2([1,2,3])

#subsets 2 duplicate elements
def subsetsdup(array):
    res = [[]]
    if len(array)==0:
        return res
    generate2(res,[],array,0)
    return res

def generate2(res,curr,array,level):
    if level == len(array):
        return
    index = level
    while index<len(array):
        curr.append(array[index])
        res.append(curr[:])
        generate2(res,curr,array,index+1)
        curr.pop()
        while index <len(array)-1 and array[index]==array[index+1]:
            index +=1
        index += 1

print subsetsdup([1,2,2])

######################### permutation
#---------------------------------------permutation
def getperm(array):
    return [c for c in it.permutations(array)]

print getperm([1,2,3])

def getperm2(array):
    res =[]
    if len(array)==0:
        return res
    isvisited = [False]*len(array)
    backtracking2(res,[],isvisited, array)
    return res

def backtracking2(res, curr, isvisited,array):
    if len(curr) == len(array):
        res.append(curr[:])
        return
    for i in range(len(array)):
        if isvisited[i]==False:
            isvisited[i]=True
            curr.append(array[i])
            backtracking2(res,curr,isvisited,array)
            isvisited[i]=False
            curr.pop()
    return 
    
print getperm2([1,2,3])

#permutation2 duplicate elements sorted
def getpermdup(array):
    res =[]
    if len(array)==0:
        return res
    isvisited = [False]*len(array)
    backtracking3(res,[],isvisited, array)
    return res

def backtracking3(res, curr, isvisited,array):
    if len(curr) == len(array):
        res.append(curr[:])
        return
    i=0
    while i<len(array):
        if isvisited[i]==False:
            isvisited[i]=True
            curr.append(array[i])
            backtracking3(res,curr,isvisited,array)
            isvisited[i]=False
            curr.pop()
            while i<len(array)-1 and array[i]==array[i+1]:
                i+=1   
        i+=1
    return 
    
print getpermdup([1,2,2,3])






