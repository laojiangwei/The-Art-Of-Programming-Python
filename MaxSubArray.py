#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-08 15:21:25
# @Author: Lao Jiangwei
# @Version : $Id$
'''
输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。 求所有子数组的和的最大值，要求时间复杂度为O(n)。
例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2， 因此输出为该子数组的和18。
'''
#解法一
'''
求一个数组的最大子数组和，我想最直观最野蛮的办法便是，三个for循环三层遍历，求出数组中每一个子数组的和，最终求出这些子数组的最大的一个值。 令currSum[i, …, j]为数组A中第i个元素到第j个元素的和（其中0 <= i <= j < n），maxSum为最终求到的最大连续子数组的和。
'''
def MaxSubArray1(allnum):
    maxnum=allnum[0]
    for i in range(len(allnum)):
        for j in range(i,len(allnum)):
            sumnumber=0
            for k in range(i,j+1):
                sumnumber+=allnum[k]
            if sumnumber>maxnum:
                maxnum=sumnumber
    return maxnum
#解法二
'''
事实上，当我们令currSum为当前最大子数组的和，maxSum为最后要返回的最大子数组的和，当我们往后扫描时，
对第j+1个元素有两种选择：要么放入前面找到的子数组，要么做为新子数组的第一个元素；
如果currSum加上当前元素a[j]后不小于a[j]，则令currSum加上a[j]，否则currSum重新赋值，置为下一个元素，即currSum = a[j]。
同时，当currSum > maxSum，则更新maxSum = currSum，否则保持原值，不更新。
'''
def MaxSubArray2(allnum):
    maxsum=allnum[0]
    sumnumber=allnum[0]
    for i in range(1,len(allnum)):
        sumnumber=max(sumnumber+allnum[i],allnum[i])
        maxsum=max(maxsum,sumnumber)
    return maxsum
if __name__ == '__main__':
    allnum=[1, -2, 3, 10, -4, 7, 2, -5]
    print(MaxSubArray1(allnum))
    print(MaxSubArray2(allnum))
    