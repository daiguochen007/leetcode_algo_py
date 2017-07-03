#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:29:06 2017

this is a test set for Dynamic Programming dp[i][j]=f(dp[i-1][j-1]...)

@author: guochendai
"""


# ------------------------------ best time to buy or sell stock (one trade)
price = [1,1.1,1.05,0.98,0.99,1.2,1.3,1.5,1.53,1.48]

def maxprofit(price): #O(N)
    if len(price)<=1:
        return 0
    if len(price)==2:
        return abs(price[1]-price[0])
    else:
        minprice = price[0]
        maxprice = price[0]
        maxbuyprofit = 0
        maxsellprofit = 0
        for i in range(1,len(price)):
            profit = price[i] - minprice 
            if profit > maxbuyprofit:
                maxbuyprofit = profit
            profit =  maxprice - price[i]     
            if profit > maxsellprofit:
                maxsellprofit = profit            
            if price[i]< minprice:
                minprice = price[i]
            if price[i]> maxprice:
                maxprice = price[i]
        return max(maxbuyprofit,maxsellprofit)

print maxprofit(price)

# best time to buy or sell stock 2 (multiple trades)
def maxprofit2(price):
    profit = 0
    for i in range(1,len(price)):
        profit += abs(price[i]-price[i-1])
    return profit

print maxprofit2(price)

# best time to buy or sell stock 3 (at most two trades)
def maxprofit3(price): #O(N)
    profit = 0
    for i in range(1,len(price)-1):
        first_vec = price[:i+1]
        second_vec = price[i:]
        if maxprofit(first_vec)+maxprofit(second_vec)> profit:
            profit = maxprofit(first_vec)+maxprofit(second_vec)
    return profit

print maxprofit3(price)

#-----------------------------------------------unique path m*n grid
def getuniquepath(m,n):
    if m ==0 or n==0:
        return 0
    mat = [[1]*m]+[[1]+[0]*(m-1)]*(n-1)
    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]   
    return mat[n-1][m-1]

print getuniquepath(3,3)

# add obstacle grid 0 pass 1 block
# 0---0---0---0
# 0---0---1---0
# 0---0---0---0

def getuniquepath2(obstacle):
    n = len(obstacle)
    m = len(obstacle[0])
    if m ==0 or n==0:
        return 0
    mat = [[1]*m]+[[1]+[0]*(m-1)]*(n-1)
    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] = mat[i-1][j] + mat[i][j-1] 
            if obstacle[i][j]==1:
                mat[i][j]=0
    return mat[n-1][m-1]

print getuniquepath2([[0,0,0,0],[0,0,1,0],[0,0,0,0]])

# add obstacle grid 0 pass 1 block
# 1---2---5--- 7
# 3---4---10---2
# 1---2---99---6
def minpathsum(grid):
    n = len(grid)
    m = len(grid[0])
    if m ==0 or n==0:
        return 0
    mat = grid[:][:]
    for i in range(1,n):
        mat[i][0] += mat[i-1][0]
    for j in range(1,m):
        mat[0][j] += mat[0][j-1]
    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] += min(mat[i-1][j],mat[i][j-1])
    return mat[n-1][m-1]

print minpathsum([[1,2,5,7],[3,4,10,2],[1,2,99,6]])

#----------------------------------------------- max subarray
array = [1,1.0/50,4,-5,1,2,0,-1,6,-5,1.0/3.0,4]

#maxsum
def maxsumsubarray(array):
    maxsum = 0
    temp = 0
    for i in range(len(array)):
        temp += array[i]
        if temp< 0:
            temp =0
        maxsum = max(temp,maxsum)
    return maxsum

print maxsumsubarray(array)

#max product
def maxprodsubarray(array):
    maxvalue = 0
    temp = 1
    for i in range(len(array)):
        temp *= array[i]
        maxvalue = max(temp,maxvalue)
        if temp>-1 and temp < 1:
            temp =1  
    return maxvalue

print maxprodsubarray(array)

#----------------------------------------------- climb stairs n stairs 1 or 2 step once a time, how many paths
def getstair(n):
    if n<=2:
        return n
    else:
        a=1
        b=2
        for i in range(3,n+1):
           b,a=a+b,b
        return b
                
print getstair(5)

#----------------------------------------------- search min sum path for triangle  O(N) space
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

def minsumtri(triangle):
    n = len(triangle)
    if n==1:
        return triangle[0][0]
    if n==2:
        return max(triangle[0][0]+triangle[1][0],triangle[0][0]+triangle[1][1])
    else:
        res = [0]*n
        res[0] = triangle[0][0]
        res[1] = triangle[1][1] + res[0]
        res[0] = triangle[1][0] + res[0]
        for j in range(2,n):
            res[j] = res[j-1]+triangle[j][j]
            for i in range(j-1,0,-1):
                res[i] = min(res[i]+triangle[j][i],res[i-1]+triangle[j][i])
            res[0] = res[0]+triangle[j][0]
        return min(res)

print minsumtri(triangle)

#----------------------------------------------- unique binary search trees 1:n
#   1    1     2    3     3   
#  ---  ---   ---  ---   ---
#    3    2   1 3  1     2
#   ---  ---       ---   ---
#   2      3         2   1

def numTrees(n):
    dp = [1,1]
    for i in range(2,n+1):
        dp.append(0)
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

print numTrees(3)

#------------------------------------------------ integer by sum of perfect squares(min num)
# 12 = 4+4+4 (3)
# should not start from largest square 12 = 9+1+1+1 (4)
def numSquares(n):
    dp = [0]+[1000000]*n
    for i in range(n+1):
        for j in range(1,int((n-i)**0.5)+1):
            dp[i+j*j] = min(dp[i+j*j],dp[i]+1)
    return dp[n]

print numSquares(12)





