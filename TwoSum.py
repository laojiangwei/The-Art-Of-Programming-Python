#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-06 19:11:49
# @Author: Lao Jiangwei
# @Version : $Id$
'''
输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。
要求时间复杂度是O(N)。如果有多对数字的和等于输入的数字，输出任意一对即可。
例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。
'''
'''
如果数组是无序的，先排序(N log N)，然后用两个指针i，j，各自指向数组的首尾两端，令i=0，j=n-1，然后i++，j--，逐次判断a[i]+a[j]?=sum，
如果某一刻a[i]+a[j] > sum，则要想办法让sum的值减小，所以此刻i不动，j--；
如果某一刻a[i]+a[j] < sum，则要想办法让sum的值增大，所以此刻i++，j不动。
所以，数组无序的时候，时间复杂度最终为O(N log N + N)=O(N log N)。
如果原数组是有序的，则不需要事先的排序，直接用两指针分别从头和尾向中间扫描，O(N)搞定，且空间复杂度还是O(1)。
'''
def TwoSum(allnumber,sum):
    begin=0
    end=len(allnumber)-1
    while(begin<end):
        if allnumber[begin]+allnumber[end]==sum:
            print(allnumber[begin],allnumber[end])
            return
        else:
            if allnumber[begin]+allnumber[end]<sum:
                begin+=1
            else:
                end-=1
    print('None')


if __name__ == '__main__':
    allnumber=[1,2,4,7,11,15]
    allnumber.sort
    TwoSum(allnumber,15)