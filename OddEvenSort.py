#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-10 16:41:53
# @Author: Lao Jiangwei
# @Version : $Id$

#题目描述
'''
输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。要求时间复杂度为O(n)。
'''
#解法一
'''
利用快速排序的思想，第一种是建立两个指针，从两边到中间遍历
'''
def OddEvenSort1(allnumber):
    begin=0
    end=len(allnumber)-1
    while(begin<end):
        if allnumber[begin]%2==1:
            begin+=1
        elif allnumber[end]%2==0:
            end-=1
        else:
            temp=allnumber[begin]
            allnumber[begin]=allnumber[end]
            allnumber[end]=temp

#解法二
'''
利用快速排序的思想，第二种是建立两个指针，从左至右扫描一遍
'''
def OddEvenSort2(allnumber):
    point_a=-1
    for point_b in range(len(allnumber)):
        if allnumber[point_b]%2==1:
            point_a+=1
            temp=allnumber[point_a]
            allnumber[point_a]=allnumber[point_b]
            allnumber[point_b]=temp
            continue
        else:
            pass


if __name__ == '__main__':
    allnumber=[2,8,7,1,3,5,6,4]
    OddEvenSort1(allnumber)
    print(allnumber)
    allnumber=[2,8,7,1,3,5,6,4]
    OddEvenSort2(allnumber)
    print(allnumber)