#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:51:23 2017

A training set on "trees" 

@author: guochendai
"""

#---------------------------------------- Tree node definition
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

#       1
#   --------
#   2       3
# -----   -----
# 4   5   6   7
#---------------- make tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
#add complexity
#         1
#     --------
#     2       3
#   -----   -----
#   4   5   6   7
# ---  ---     -----
# 8      9    10   11
#                 -----
#                     12
root.left.left.left = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)
root.right.right.right.right = Node(12)



#--------------------------------------------- pre&in&post order the tree
#recursive
def preOrder(root):
    if root:
        preodr_vec.append(root.data)
        preOrder(root.left)
        preOrder(root.right)
#stack       
def preOrder2(root):
    if root==None:
        return None
    stack = []
    values = []
    node = root
    while node or stack:
        while node:                     #从根节点开始，一直找它的左子树
            values.append(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
        node = node.right
    return values

#recursive
def inOrder(root):
    if root:      
        inOrder(root.left)
        inodr_vec.append(root.data)
        inOrder(root.right)

#stack       
def inOrder2(root):
    if root==None:
        return None
    stack = []
    values = []
    node = root
    while node or stack:
        while node:                     #从根节点开始，一直找它的左子树           
            stack.append(node)
            node = node.left
        node = stack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
        values.append(node.data)
        node = node.right
    return values

#recursive
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        postodr_vec.append(root.data)        

#stack       
def postOrder2(root):
    if root==None:
        return None
    stack = []
    values = []
    node = root
    while node or stack:
        while node:                     #从根节点开始，一直找它的right子树
            values.append(node.data)
            stack.append(node)
            node = node.right
        node = stack.pop()            #while结束表示当前节点node为空，即前一个节点没有right子树了
        node = node.left
    values.reverse()
    return values


preodr_vec=[]
inodr_vec=[]
postodr_vec=[]

preOrder(root)
inOrder(root)
postOrder(root)

preOrder2(root)
inOrder2(root)
postOrder2(root)


#------------------------------------------------------------ level order traversal
# recursive
def levelorder(root):
    if root==None:
        return None
    result=[]
    getsolution(result,root,1)
    return result

def getsolution(result,root,level):
    if root==None:
        return
    if len(result)<level:
        result.append([])
    result[level-1].append(root.data)
    getsolution(result,root.left,level+1)
    getsolution(result,root.right,level+1)    

print levelorder(root)

#queue
def levelorder2(root):
    if root==None:
        return None
    result=[]
    myQueue=[]
    node = root
    myQueue.append(node)
    while myQueue:
        node = myQueue.pop(0)
        result.append(node.data)
        if node.left!=None:
            myQueue.append(node.left)
        if node.right!=None:
            myQueue.append(node.right)           
    return result

print levelorder2(root)


#----------------------------------------------------------- treeheight
#max
def maxdepth(root):
    if root is None:
        return 0
    h_left = maxdepth(root.left)
    h_right = maxdepth(root.right)
    
    if h_left >= h_right:
        return h_left+1
    else:
        return h_right+1

def travel(root,level,num):
    if root.left==None and root.right==None:
        return max(num,level)
    if root.left!=None and root.right!=None:
        return max(travel(root.left,level+1,num),travel(root.right,level+1,num))
    if root.left!=None:
        return travel(root.left,level+1,num)
    if root.right!=None:
        return travel(root.right,level+1,num)
def maxdepth2(root):
    if root is None:
        return 0
    return travel(root,1,1)

print maxdepth(root)
print maxdepth2(root)

#------------------min
def travel2(root,level,num):
    if root.left==None and root.right==None:
        return min(num,level)
    if root.left!=None and root.right!=None:
        return min(travel2(root.left,level+1,num),travel2(root.right,level+1,num))
    if root.left!=None:
        return travel2(root.left,level+1,num)
    if root.right!=None:
        return travel2(root.right,level+1,num)
def mindepth2(root):
    if root is None:
        return 0
    return travel2(root,1,1000000)
    
print mindepth2(root)

#--------------------------------------------------construct tree from in and post order
def build(inodr_vec,s0,e0,postodr_vec,s1,e1):
    m = dict([(data,i) for i,data in enumerate(inodr_vec)])  
    if s0>e0 or s1>e1:
        return None
    root = Node(postodr_vec[e1])
    
    mid = m[postodr_vec[e1]]
    num = mid-s0
    
    root.left = build(inodr_vec,s0,mid-1,postodr_vec,s1,s1+num-1)
    root.right = build(inodr_vec,mid+1,e0,postodr_vec,s1+num,e1-1)
    return root

def buildtree(inodr_vec,postodr_vec):
    if postodr_vec==[]:
        return None   
    return build(inodr_vec,0,len(inodr_vec)-1,postodr_vec,0,len(postodr_vec)-1)

#check
root = buildtree(inodr_vec,postodr_vec)
preodr_vec=[]
preOrder(root)
# from from pre and in order 
def build2(preodr_vec,s0,e0,inodr_vec,s1,e1):
    m = dict([(data,i) for i,data in enumerate(inodr_vec)])  
    if s0>e0 or s1>e1:
        return None
    root = Node(preodr_vec[s0])
    
    mid = m[preodr_vec[s0]]
    num = mid-s1
    
    root.left = build2(preodr_vec,s0+1,s0+num,inodr_vec,s1,mid-1)
    root.right = build2(preodr_vec,s0+num+1,e0,inodr_vec,mid+1,e1)
    return root

def buildtree2(preodr_vec,inodr_vec):
    if preodr_vec==[]:
        return None   
    return build2(preodr_vec,0,len(preodr_vec)-1,inodr_vec,0,len(inodr_vec)-1)

#check
root = buildtree2(preodr_vec,inodr_vec)
postodr_vec=[]
postOrder(root)
    
# ---------------------------------------------------------Is Symmetric tree
#recursive
def helper(left,right):
    if left==None and right==None:
        return True
    elif left==None or right==None:
        return False
    return left.data==right.data and helper(left.left,right.right) and helper(left.right,right.left)

def isSymmetric(root):
    if root==None:
        return True
    return helper(root.left,root.right)

#------- make tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(2)
root.right.right = Node(4)
#         1
#     --------
#     2      2
#   -----   ----
#   4          4

print isSymmetric(root)

def isSymmetric2(root):
    if root == None:
        return True
    if root.left== None and root.right == None:
        return True
    if (root.left!= None and root.right == None) or (root.left== None and root.right != None):
        return False
    q1=[]
    q2=[]
    q1.append(root.left)
    q2.append(root.right)
    while q1 != [] and q2 !=[]:
        n1 = q1.pop(0)
        n2 = q2.pop(0)
        if (n1!= None and n2 == None) or (n1== None and n2 != None):
            return False
        if n1!= None and n2!= None:
            if n1.data!=n2.data:
                return False
            q1.append(n1.left)
            q1.append(n1.right)
            q2.append(n2.right)
            q2.append(n2.left)
    return True

print isSymmetric2(root)

# ------------------------------------------------------------------------------Is Same tree
def isSame(root1,root2):
    if root1== None and root2 == None:
        return True
    if (root1 != None and root2 == None) or (root1 == None and root2 != None):
        return False
    if root1.data==root2.data:
        left = isSame(root1.left,root2.left)
        right = isSame(root1.right,root2.right)
        return left and right
    return False

print isSame(root,root)

# ------------------------------------------------------------------------------Is Balanced tree
# a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of 
# every node never differ by more than 1.

def isBalanced(root):
    if root==None:
        return True
    if getheight(root)!= -1:
        return True
    else:
        return False

def getheight(root):
    if root==None:
        return 0
    leftheight = getheight(root.left)
    if leftheight==-1:
        return -1
    rightheight = getheight(root.right)
    if rightheight==-1:
        return -1
    diffheight = abs(rightheight - leftheight)
    if diffheight>1:
        return -1
    else:
        return max(rightheight,leftheight)+1

print isBalanced(root)

# -------------------------------------------------------------------------------- path sum

def haspathsum(root,target):
    if root == None:
        return False
    return DFS(target,0,root)

def DFS(target,pathsum,root):
    if root == None:
        return False
    pathsum += root.data
    if root.left==None and root.right==None:
        if pathsum==target:
            return True
        else:
            return False
    leftpart = DFS(target,pathsum,root.left)
    rightpart = DFS(target,pathsum,root.right)
    return leftpart or rightpart

#       1
#   --------
#   7      4
# -----   -----
# 6   2   5   9
#---------------- make tree
root = Node(1)
root.left = Node(7)
root.left.left = Node(6)
root.left.right = Node(2)
root.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(9)

print haspathsum(root,10)    
    
def pathsum(root,target):
    if root == None:
        return []
    path=[]
    allpath = []
    DFS2(root,target,path,allpath)
    return allpath

def DFS2(root,target,path,allpath):
    if root == None:
        return
    elif root.left==None and root.right==None:
        if sum(path)+root.data==target:
            path.append(root.data)
            allpath.append(path[:])
            path.pop()
    else:
        path.append(root.data)
        DFS2(root.left,target,path,allpath)
        DFS2(root.right,target,path,allpath)
        path.pop()

print pathsum(root,10)

# ----------------------------------------------------valid tree(left<=root<=right)

def isvalidtree(root):
    if root== None:
        return True
    
    if root.left!= None:
        if root.left.data<=root.data:
            return isvalidtree(root.left)
        else:
            return False
    if root.right!= None:
        if root.right.data>=root.data:
            return isvalidtree(root.right)
        else:
            return False
    return True

#       3
#   --------
#   2       6
# -----   -----
# 1   5   7   8
#---------------- make tree
root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)

print isvalidtree(root)
    
# ----------------------------------------------------binary tree path
#Given a binary tree, return all root-to-leaf paths.

def gettreepath(root):
    if root==None:
        return []
    allpath = []
    path = []
    DFSpath(root,path,allpath)
    return allpath

def DFSpath(root,path,allpath): 
    if root==None:
        return
    path.append(root.data)
    if root.left==None and root.right==None:
        allpath.append(path[:])
        path.pop()
        return
    if root.left!=None:
        DFSpath(root.left,path,allpath)
    if root.right!=None:
        DFSpath(root.right,path,allpath)
    path.pop()
    
print gettreepath(root)   

#roof to leaf numbers 1->2->3 = 123
def getnum(root):
    if root==None:
        return []
    allpath = []
    path = []
    DFSpath(root,path,allpath)
    for i in range(len(allpath)):
        allpath[i] = int("".join(map(str,allpath[i])))
    return allpath

print getnum(root) 




