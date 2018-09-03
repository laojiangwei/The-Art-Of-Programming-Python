#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-03 16:22:22
# @Author: Lao Jiangwei
# @Version : $Id$
'''
题目描述
输入n个整数，输出其中最小的k个。
'''

# 解法一、利用快速排序对序列进行排序，输出前面最小的k个数。
# 为了更好的理解算法，没有用sort()函数

def QKSORT_TopMinK(numberlist,k):
    def QKSOR(numberlist,lo,hi):
        if hi<=lo:
            return
        lt=lo
        i=lo+1
        gt=hi
        v=numberlist[lo]
        while(i<=gt):
            if numberlist[i]<v:
                numberlist[i],numberlist[lt]=numberlist[lt],numberlist[i]
                i+=1
                lt+=1
            elif numberlist[i]>v:
                numberlist[i],numberlist[gt]=numberlist[gt],numberlist[i]
                gt-=1
            else:
                i+=1
        QKSOR(numberlist,lo,lt-1)
        QKSOR(numberlist,gt+1,hi)
    QKSOR(numberlist,0,len(numberlist)-1)
    print(numberlist[:k])

# 解法二、
# 第一步、拿出k个数，找出k个数的最大值maxk
# 第二步、将maxk与余下的n-k个数比较，找出比maxk小的数，并替换，直至找不到比他小的数

def SLSORT_TopMinK(numberlist,k):
    def SLSORT(numberlist,k):
        maxk=max(numberlist[:k])
        index_maxk=numberlist.index(maxk)
        for i in range(k,len(numberlist)):
            if numberlist[i]<maxk:
                numberlist[i],numberlist[index_maxk]=numberlist[index_maxk],numberlist[i]
                return True
            else:
                pass
        return False
    while(SLSORT(numberlist,k)):
        pass
    print(numberlist[:k])

# 解法三、
# 解法三和解法二类似，只是解法二的第二步可以用堆来实现，可以调用heapq来实现，但是为了更加深入理解堆，我们手动构造一个功能简单的堆。

def HEAPSORT_TopMinK(numberlist,k):
    def sink(x):
        while 2*x+1<=k-1:
            i=2*x+1
            if i<k-1 and numberlist[i]<numberlist[i+1]:
                i+=1
            if numberlist[x]<numberlist[i]:
                numberlist[x],numberlist[i]=numberlist[i],numberlist[x]
                x=i
            else:
                break
    def swim(x):
        while int((x-1)/2)>=0:
            i=int((x-1)/2)
            if numberlist[i]<numberlist[x]:
                numberlist[x],numberlist[i]=numberlist[i],numberlist[x]
                x=i
            else:
                break
    def SLSORT():
        for i in range(k,len(numberlist)):
            if numberlist[i]<numberlist[0]:
                numberlist[i],numberlist[0]=numberlist[0],numberlist[i]
                sink(0)
                return True
            else:
                pass
        return False
    for i in range(int(k/2),-1,-1):
        sink(i)
    while(SLSORT()):
        pass
    print(numberlist[:k])

#解法四、快速选择法，利用快去排序的思路，找到第k小的数

def QuickSelct_TopMinK(numberlist,k):
    def QuickSelct(lo,hi):
        if hi<=lo:
            return
        pivot=numberlist[lo]
        lt=lo+1
        gt=hi
        while lt<=gt:
            while numberlist[lt]<=pivot:
                lt+=1
            while numberlist[gt]>pivot:
                gt-=1
            if lt<=gt:
                numberlist[lt],numberlist[gt]=numberlist[gt],numberlist[lt]
                lt+=1
                gt-=1
        numberlist[lo],numberlist[gt]=numberlist[gt],numberlist[lo]
        if gt==k-1:
            return
        elif gt>k-1:
            QuickSelct(lo,gt-1)
        else:
            QuickSelct(gt+1,hi)
    QuickSelct(0,len(numberlist)-1)
    print(numberlist[:k])


if __name__ == '__main__':
    numberlist=[2,3,2,4,1,3,5,2,3,4,6,12,3,15,12]
    #解法一
    QKSORT_TopMinK(numberlist,8)
    #解法二
    SLSORT_TopMinK(numberlist,8)
    #解法三
    HEAPSORT_TopMinK(numberlist,8)
    #解法四
    QuickSelct_TopMinK(numberlist,8)