#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:16:30 2017

A traing set on "Arrays"

@author: guochendai
"""

array =[1,2,3,4,5,2,3,2,3,5,7,9,2]

#------------remove element 2
filter(lambda x:x!=2,array)

#---------------- remove duplicates
def removedup(array):
    d = {}
    for num in array:
        if d.has_key(num):
            d[num] +=1
        else:
            d[num]=1
    return d.keys()

print removedup(array)

#remove n duplicates
def removedupn(array,n):
    d = {}
    for num in array:
        if d.has_key(num):
            d[num] +=1
        else:
            d[num]=1
    res = []
    for (k,v) in d.items():
        if v<=n:
            res += [k]*v        
    return res

print removedupn(array,2)

#-------------------------------pascal triangle
def getpascal(n):
    if n==0:
        return []
    if n==1:
        return [[1]]
    if n==2:
        return [[1],[1,1]]
    res = [[1],[1,1]]
    for i in range(2,n):
        layer=[]
        layer.append(1)
        for j in range(1,i):
            layer.append(res[i-1][j-1]+res[i-1][j])
        layer.append(1)
        res.append(layer)      
    return res

getpascal(5)

def getpascallayer(n): #O(n) space
    if n==0:
        return []
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    res = [1,1]
    for i in range(2,n):
        res.append(1)
        for j in range(i-1,0,-1):
            res[j] += res[j-1]  
    return res

getpascallayer(5)

#---------------------------------------two sum
array =[1,2,3,4,5,6,7] #distinct

#return index can't sort
def twosum(array,target):
    d={}
    res = []
    for i in range(len(array)):
        d[array[i]] = i
    for i in range(len(array)):
        if array[i]< target/2.0:  # for sorted array
            if d.has_key(target - array[i]):
                temp = sorted([d[array[i]],d[target - array[i]]])
                res.append(temp)
    return res
    
print twosum(array,8)

#return number can sort
def threesum(array,target):
    d={}
    res = []
    for i in range(len(array)):
        d[array[i]] = i
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if d.has_key(target - array[i]-array[j]) and target - array[i]-array[j]!= array[i] and target - array[i]-array[j]!= array[j]:
                temp = sorted([array[i],array[j],target - array[i]-array[j]])
                if res.count(temp)==0:
                    res.append(temp)
    return res
    
print threesum(array,10)

#--------------------------------------------rotated sorted array
array =[5,6,7,1,2,3,4]

def getmin(array):
    if len(array)==0:
        return None
    if len(array)==1:
        return array[0]
    if len(array)==2:
        return min(array[1],array[0])
    start = 0
    end = len(array)-1
    
    while start<end -1:
        mid = start + (end-start)/2
        
        if array[start]< array[mid]:
            start = mid
        else:
            end = mid
    return min(array[start],array[end])
        
getmin(array)

#-------------------------------------------- largest rectange   O(N)
array =[2,1,5,6,2,3]

def maxRectArea(array): 
    stack=[]
    i=0
    area=0
    while i<len(array):
        if stack==[] or array[i]>array[stack[len(stack)-1]]:
            stack.append(i)
        else:
            curr=stack.pop()
            width=i if stack==[] else i-stack[len(stack)-1]-1
            area=max(area,width*array[curr])
            i-=1
        i+=1
    while stack!=[]:
        curr=stack.pop()
        width=i if stack==[] else len(array)-stack[len(stack)-1]-1
        area=max(area,width*array[curr])
    return area

maxRectArea(array)

#-------------------------------------------- palindrome number 1234321
def ispalindrome(num):
    if num<0:
        return False
    if num==0:
        return True
    tmp = num
    y=0
    while tmp!=0:
        y=y*10+tmp%10
        tmp=tmp/10
    if y==num:
        return True
    else:
        return False

ispalindrome(12345654321)

#-------------------------------------------- search in a 2D matrix (sorted both horizntal and vertical) go daignoal 

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
mat = [[1,3,5],[10,11,16],[23,30,34],[25,31,50]]

def getpos(mat,value):
    n = len(mat)
    m = len(mat[0])
    for i in range(1,min(n,m)):
        if mat[i-1][i-1] == value:
            return [i-1,i-1]
        if mat[i-1][i-1] < value < mat[i][i]:
            for k in range(i,m):
                if mat[i-1][k] == value:
                    return [i-1,k]
            for k in range(i,n):
                if mat[k][i-1] == value:
                    return [k,i-1]
    if n<=m:
        for k in range(n-1,m):
            if mat[n-1][k] == value:
                return [n-1,k]
    else:
        for k in range(m-1,n):
            if mat[k][m-1] == value:
                return [k,m-1]
    return []

getpos(mat,50)

#-------------------------------------------- search duplicate element start end from array 二分法 O(logN)
array =[1,2,2,3,4,5,5,5,5,7,8,8,9]

def getelem(array,num):
    start=0
    end= len(array)-1
    while start<=end:
        mid = start + (end-start)/2
        if array[mid] < num:
            start = mid+1
        else:
            end = mid-1
    firstnum = start
    end= len(array)-1
    while start<=end:
        mid = start + (end-start)/2
        if array[mid] <= num:
            start = mid+1
        else:
            end = mid-1 
    return [firstnum,start-1]   
        
print getelem(array,2)


#-------------------------------------------- search insert position in array, exist return postion 二分法  O(logN)
array =[1,2,3,6,8,9,11,15]

def getinsertpos(array,num):
    start=0
    end= len(array)-1
    while start<=end:
        mid = start + (end-start)/2
        if array[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return start 
        
print getinsertpos(array,14)

#-------------------------------------------- get peak element in array 二分法 O(logN)
array =[1,2,3,4,5,9,11,10]

def findpeakelem(array):
    if len(array)==1:
        return 0
    start=0
    end= len(array)-1
    while start<=end:
        mid = start + (end-start)/2
        if (mid==0 or array[mid]>=array[mid+1]) and (mid==len(array)-1 or array[mid]>= array[mid+1]):
            return mid
        elif mid>0 and array[mid] < array[mid-1]:
            end = mid-1
        else:
            start = mid+1
    return mid
        
print findpeakelem(array)
