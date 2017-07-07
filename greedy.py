#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:53:42 2017

This is a test set on greedy

@author: guochendai
"""

#------------------------------------- jump game
#Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.
#For example: A = [2,3,1,1,4], return true.
#A = [3,2,1,0,4], return false.

def canjump(array):
    if len(array)==0:
        return
    temp = array[0]
    for i in range(1,len(array)):
        temp -= 1
        if temp<0:
            return False
        
        if temp< array[i]:
            temp = array[i]
            
    return True

print canjump([2,3,1,1,1,0,4])

#jump game 2 return min jumps
#Your goal is to reach the last index in the minimum number of jumps.

def min_numjump(array):
    if len(array)==0:
        return
    step = 0
    cur_ = 0
    next_ = 0
    i=0
    while i < len(array):
        if cur_>= len(array)-1:
            break
        while i<= cur_:
            next_ = max(next_,array[i]+i)
            i+=1
        step+=1
        cur_ = next_          
    return step

print min_numjump([2,8,1,1,1,4])

#------------------------------------- gas station unique solution
#There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
#You begin the journey with an empty tank at one of the gas stations.
#Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#Note: The solution is guaranteed to be unique.

def index_Circuit(gas_arr,cost_arr):
    if sum(gas_arr)<sum(cost_arr):
        return -1   
    start = 0
    total_gas = 0
    for i in range(len(gas_arr)):
        total_gas += gas_arr[i] - cost_arr[i]
        if total_gas< 0:
            start = i + 1
            total_gas = 0
    return start

index_Circuit([2,5,4],[3,4,2])

#------------------------------------- candy
#There are N children standing in a line. Each child is assigned a rating value. 
#You are giving candies to these children subjected to the following requirements:
#Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. 
#What is the minimum candies you must give?

def candy(rating_arr):
    n = len(rating_arr)
    result = [1]* n
    for i in range(n-1):
        if rating_arr[i]< rating_arr[i+1]:
            result[i+1] = result[i]+1
    for i in range(n-1,0,-1):
        if rating_arr[i]< rating_arr[i-1] and result[i]>=result[i-1]:
            result[i-1] = result[i]+1   
    return result

print candy([1,2,3,4,2,2,3,2,1,1,3,2,1])

#------------------------------------- word break
#Given a string s and a dictionary of words dict, determine if s can be segmented into a space- separated sequence of one or more dictionary words.
#For example, given s = "leetcode", dict = ["leet", "code"].
#Return true because "leetcode" can be segmented as "leet code".

def wordbreak(s, words):
    d = [False] * len(s)    
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]

print wordbreak("leetcode", ["leet","code"])

#word break 2 
#Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#Return all such possible sentences.
#For example, given s = "catsanddog", dict = ["cat", "cats", "and", "sand", "dog"]. 
#A solution is ["cats and dog", "cat sand dog"].

def wordbreak2(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return helper(s, wordDict, {})
    
def helper(s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res

wordbreak2("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    






