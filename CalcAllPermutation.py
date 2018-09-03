#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-03 14:57:49
# @Author: Lao Jiangwei
# @Version : $Id$
'''
题目描述
输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串
abc、acb、bac、bca、cab 和 cba。
'''
#解法一、递归实现
#每次从数组中选组一个元素作为排列的第一个元素，然后对剩下的元素进行全排列，如此递归处理，直到得到所有元素的全排列。
def CalcAllPermutation1(alllist,form,to):
    if to<=1:
        return
    if form==to:
        print(alllist)
    else:
        for i in range(form,to+1):
            alllist[i],alllist[form]=alllist[form],alllist[i]
            CalcAllPermutation1(alllist,form+1,to)
            alllist[i],alllist[form]=alllist[form],alllist[i]

#解法二、字典序排列
#每次从当前排列的字符串生成字典序刚好比他大的下一个排列

def CalcAllPermutation2(alllist):
    pointer1=-1
    for i in range(len(alllist)-1):
        if alllist[-1-i]>alllist[-1-i-1]:
            pointer1=i+1
            break
        else:
            pass
    if pointer1==-1:
        return False
    for i in range(pointer1):
        if alllist[-1-i]>alllist[-1-pointer1]:
            pointer2=i
            break
        else:
            pass
    alllist[-1-pointer1],alllist[-1-pointer2]=alllist[-1-pointer2],alllist[-1-pointer1]
    alllist[-1-pointer1+1:]=alllist[-1:-1-pointer1:-1]
    print(alllist)
    return True

if __name__ == '__main__':
    alllist=['a','b','c','d','e','f']
    #解法一、递归实现
    CalcAllPermutation1(alllist,0,len(alllist)-1)
    #解法二、字典序排列
    while(CalcAllPermutation2(alllist)):
        pass