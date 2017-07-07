#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:55:23 2017

This is a test set on linked list 双指针法

@author: guochendai
"""
#define linked list node

class Node:
    def __init__(self,data,right=None):
        self.data = data
        self.right = right

#depth of linked list, hascycle needed
def len_linklist(root):
    if hascycle(root):
        print "has cycle!"
        return 
    res = 0
    start = root
    while start!=None:
        res += 1
        start=start.right
    return res

#get string of linked list, hascycle needed
def str_linklist(root):
    if root == None:
        return
    if hascycle(root):
        print "has cycle!"
        return 
    res=[]
    start = root
    while start!=None:
        res.append(str(start.data))
        start=start.right
    return "->".join(res)

#set cycle
root = Node(1,Node(2,Node(3,Node(4,None))))
print str_linklist(root)
#cycle
root.right.right.right.right = root.right
#         --------
#        |        |
#   1 -> 2 ->3 -> 4

#------------------------------------if Linked List has Cycle
def hascycle(root):
    if root==None or root.right == None:
        return False
    fast = root
    slow = root
    while fast.right != None and fast.right.right !=None:
        fast = fast.right.right
        slow = slow.right
        if slow==fast:
            return True
    return False

hascycle(root)

#has Cycle 2 return start node of cycle
def hascycle2(root):
    if root==None or root.right == None:
        return False
    fast = root
    slow = root
    while fast.right != None and fast.right.right !=None:
        fast = fast.right.right
        slow = slow.right
        if slow==fast:
            start1 = root
            start2 = slow
            while start1!=start2:
                start1 = start1.right
                start2 = start2.right
            return start1
    return False

print hascycle2(root).data

#---------------------------------------intersection of two linked lists
#set 2 linked list
root1 = Node(1,Node(2,Node(3,Node(4,None))))
root2 = Node(5)
root2.right = Node(6)
root2.right.right = root1.right.right
#   5 -> 6 ->
#             3 -> 4          make it a cycle then ues hascycle2
#   1 -> 2 ->

def getintersect(root1,root2):
    start = root1
    while start.right != None:
        start = start.right
    start.right = root2
    res = hascycle2(root1)
    start.right = None  # disconnect cycle
    return res

print getintersect(root1,root2).data

#--------------------------------------- remove duplicates from sorted linked lists
#set 2 linked list
root = Node(1,Node(1,Node(2,Node(3,Node(3,Node(4,None))))))
print str_linklist(root)

def removeDup(root):
    start = root
    while start.right != None:
        if start.data == start.right.data:
            start.right = start.right.right
        else:
            start = start.right
    return root

print str_linklist(removeDup(root))

#remove duplicates 2 delete all if duplicate
def removeDup2(root):
    start = root
    prev = Node(0)     # technique: set a new node upfront
    prev.right = start
    res = prev   
    while start.right != None:     
        if start.data == start.right.data:
            while start.data == start.right.data:
                start.right = start.right.right
            prev.right = start.right
            start = prev.right
        else:
            prev = start
            start = start.right
    return res.right

print str_linklist(removeDup2(root))

#--------------------------------------- merge two sorted linked lists (previous nodes used, ref will change) 
#set 2 linked list
root1 = Node(1,Node(5,Node(9,Node(13,None))))
root2 = Node(2,Node(6,Node(10,Node(14,None))))

def mergelist(root1,root2):
    res = Node(0)
    curr = res
    start1 = root1
    start2 = root2
    while start1 and start2:
        if start1.data <= start2.data:
            curr.right = start1
            curr = start1
            start1 =start1.right
        else:
            curr.right = start2
            curr = start2
            start2 =start2.right
    if start1:
        curr.right = start1
    elif start2:
        curr.right = start2
    return res.right

print str_linklist(mergelist(root1,root2))

#----merge k sorted linked lists
root3 = Node(3,Node(7,Node(11,Node(15,None))))
root4 = Node(4,Node(8,Node(12,Node(16,None))))

def mergeNlist(root_list):
    if root_list ==None:
        return None
    n= len(root_list)
    while n>1:
        k = int((n+1)/2)
        for i in range(int(n/2)):
            root_list[i] = mergelist(root_list[i],root_list[i+k])
        n = k
    return root_list[0]

print str_linklist(mergeNlist([root1,root2,root3,root4]))

#--------------------------------------- reverse linked lists for given position range
root = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,None))))))))
str_linklist(root)

def reverselist(root,start,end):
    if start>end:
        return None
    prev = Node(0)
    prev.right = root
    curr = prev
    i = 0
    while curr!= None:
        if i+1 == start:
            node_s_prev = curr
        if i == end:
            node_e_after = curr.right
        i +=1
        curr = curr.right
    curr = node_s_prev.right 
    after = node_e_after
    while curr!= node_e_after:
        temp = curr.right
        curr.right = after
        
        after = curr
        curr = temp
    node_s_prev.right = after
    return prev.right

root = reverselist(root,1,2)
print str_linklist(root)

#--------------------------------------- reverse linked lists in k group 
#reverse every k nodes
def reverseKgroup(root,k):
    for i in range(int(len_linklist(root)/k)):
        root = reverselist(root,1+k*i,k+k*i)
    return root

root = reverseKgroup(root,3)
print str_linklist(root)

#--------------------------------------- sort the list, mergelist func used O(NlogN)
root = Node(5,Node(2,Node(3,Node(8,Node(7,Node(9,Node(10,Node(0,None))))))))
str_linklist(root)

def sortlist(root):
    if root ==None or root.right ==None:
        return root
    fast = root
    slow = root
    while fast.right.right and slow.right:
        fast = fast.right.right
        slow=slow.right
    fast = slow.right
    slow.right = None
    rootleft = sortlist(root)
    rootright = sortlist(fast)
    return mergelist(rootleft,rootright)

root = sortlist(root)
str_linklist(root)

#---------------------------------------  Sort a linked list using insertion sort 插入排序 直接插入 O(N^2)
root = Node(5,Node(2,Node(3,Node(8,Node(7,Node(9,Node(10,Node(0,None))))))))
str_linklist(root)

def insertion_sortlist(root):
    if root ==None or root.right ==None:
        return root
    after = root.right
    root.right = None
    while after:
        tmp = after.right
        after.right = None
        root = insert(root,after)        
        after = tmp
    return root

def insert(root,node):     # insert one node in a sorted linklist
    dummy = Node(0)
    dummy.right = root
    start =root
    prev= dummy
    while start:
        if node.data < start.data:
            node.right = start
            prev.right = node
            return dummy.right
        prev = prev.right
        start = start.right
    prev.right = node
    return dummy.right

root = insertion_sortlist(root)
str_linklist(root)

#---------------------------------------  Rotate list
#Given a list, rotate the list to the right by k places, where k is non-negative. For example:
#Given 1->2->3->4->5->NULL and k = 2, return 4->5->1->2->3->NULL.

root = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,None))))))))
str_linklist(root)

def rightKrotate(root,k):
    n = len_linklist(root)
    if k>= n:
        return root
    dummy = Node(0)
    dummy.right = root
    prev = dummy
    start = root
    i =1
    while start:
        if i==n-k+1:
            dummy.right = start
            prev.right = None
            break
        i+=1
        start = start.right
        prev=prev.right
    
    while start:
        if start.right == None:
            start.right = root
            break
        start = start.right    
    return dummy.right

root = rightKrotate(root,3)
str_linklist(root)

#---------------------------------------  Reorder list
#Given a singly linked list L: L0→L1→...→Ln-1→Ln,
#reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→...
#You must do this in-place without altering the nodes' values. For example,
#Given {1,2,3,4}, reorder it to {1,4,2,3}.

root = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,None))))))))
str_linklist(root)

def reorder(root):
    if root ==None or root.right ==None:
        return root
    fast = root
    slow = root 
    while fast.right.right and slow.right:
        fast = fast.right.right
        slow = slow.right
    
    fast = slow.right
    slow.right =None
    #reverse list
    dummy = Node(0)
    while fast:
        n = dummy.right
        dummy.right = fast
        nn = fast.right
        fast.right =n
        fast = nn

    slow = root
    fast = dummy.right
    #merge
    while slow:
        if fast != None:
            n = slow.right
            slow.right =fast
            nn=fast.right
            fast.right =n
            fast = nn
            slow = n
        else:
            break
    return root

root = reorder(root)
str_linklist(root)

#---------------------------------------  Partition List
#Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions. For example,
#Given 1->4->3->2->5->2 and x = 3, return 1->2->2->4->3->5.

root = Node(5,Node(2,Node(3,Node(8,Node(7,Node(9,Node(10,Node(0,None))))))))
str_linklist(root)

def partitionlist(root,x):
    dummy1 = Node(0)
    dummy2 = Node(0)
    tmp1 = dummy1
    tmp2 = dummy2
    start = root
    while start:
        if start.data < x:
            tmp1.right = start
            tmp1 = tmp1.right
        else:
            tmp2.right = start
            tmp2 = tmp2.right
        start =start.right
    
    tmp2.right = None
    tmp1.right = dummy2.right
    return dummy1.right

root = partitionlist(root,4)
print str_linklist(root)







