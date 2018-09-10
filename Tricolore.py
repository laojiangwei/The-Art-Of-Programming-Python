#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-10 19:24:29
# @Author: Lao Jiangwei
# @Version : $Id$

#题目描述
'''
现有n个红白蓝三种不同颜色的小球，乱序排列在一起，请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。
'''
'''
通过前面的分析得知，这个问题类似快排中partition过程，只是需要用到三个指针：一个前指针begin，一个中指针current，一个后指针end，current指针遍历整个数组序列，当
current指针所指元素为0时，与begin指针所指的元素交换，而后current++，begin++ ；
current指针所指元素为1时，不做任何交换（即球不动），而后current++ ；
current指针所指元素为2时，与end指针所指的元素交换，而后，current指针不动，end-- 。
为什么上述第3点中，current指针所指元素为2时，与end指针所指元素交换之后，current指针不能动呢？因为第三步中current指针所指元素与end指针所指元素交换之前，如果end指针之前指的元素是0，那么与current指针所指元素交换之后，current指针此刻所指的元素是0，此时，current指针能动么？不能动，因为如上述第1点所述，如果current指针所指的元素是0，还得与begin指针所指的元素交换。
'''
def Tricolore(allnumber):
    begin=0
    end=len(allnumber)-1
    current=0
    while(current<=end):
        if allnumber[current]==0:
            temp=allnumber[begin]
            allnumber[begin]=allnumber[current]
            allnumber[current]=temp
            begin+=1
            current+=1
        elif allnumber[current]==1:
            current+=1
        elif allnumber[current]==2:
            temp=allnumber[end]
            allnumber[end]=allnumber[current]
            allnumber[current]=temp
            end-=1

if __name__ == '__main__':
    allnumber=[0,0,2,2,1,2,0,1,2,2,1,1,0,0,2,1,0,1,0,2]
    Tricolore(allnumber)
    print(allnumber)