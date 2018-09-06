#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-06 19:49:30
# @Author: Lao Jiangwei
# @Version : $Id$
'''
输入两个整数n和sum，从数列1，2，3.......n 中随意取几个数，使其和等于sum，要求将其中所有的可能组合列出来。
'''

#解法一
'''
注意到取n，和不取n个区别即可，考虑是否取第n个数的策略，可以转化为一个只和前n-1个数相关的问题。
如果取第n个数，那么问题就转化为“取前n-1个数使得它们的和为sum-n”，对应的代码语句就是sumOfkNumber(sum - n, n - 1)；
如果不取第n个数，那么问题就转化为“取前n-1个数使得他们的和为sum”，对应的代码语句为sumOfkNumber(sum, n - 1)。
'''
def SumOfkNumber1(result,suma,n):
    if suma<=0 or n<=0:
        return
    if suma==n:
        result.insert(0,n)
        print(result)
        result.pop(0)
    result.insert(0,n)
    SumOfkNumber1(result,suma-n,n-1)
    result.pop(0)
    SumOfkNumber1(result,suma,n-1)
#解法二
def SumOfkNumber2(ad,k,suma,M,X):
    X[k]=True
    if ad+k==M:
        templist=[]
        for i in range(len(X)):
            if X[i]==True:
                templist.append(i)
        print(templist)
    else:
        if ad+k+k+1<=M:
            SumOfkNumber2(ad+k,k+1,suma-k,M,X)
        if ad+k+1<=M and ad+suma-k>=M:
            X[k]=False
            SumOfkNumber2(ad,k+1,suma-k,M,X)
    X[k]=False

if __name__ == '__main__':
    #解法一
    result=[]
    SumOfkNumber1(result,10,7)
    #解法二
    X=[False for i in range(7+1)]
    suma=int((1+7)*7/2)
    SumOfkNumber2(0,1,suma,10,X)