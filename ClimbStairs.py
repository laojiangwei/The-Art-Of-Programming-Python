#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-10 16:17:37
# @Author: Lao Jiangwei
# @Version : $Id$

#题目描述
'''
一个台阶总共有n 级，如果一次可以跳1 级，也可以跳2 级。
求总共有多少总跳法，并分析算法的时间复杂度。
'''
#解法一
'''
首先考虑最简单的情况。如果只有1级台阶，那显然只有一种跳法。如果有2级台阶，那就有两种跳的方法了：一种是分两次跳，每次跳1级；另外一种就是一次跳2级。
现在我们再来讨论一般情况。我们把n级台阶时的跳法看成是n的函数，记为f(n)。
当n>2时，第一次跳的时候就有两种不同的选择：
一是第一次只跳1级，此时跳法数目等于后面剩下的n-1级台阶的跳法数目，即为f(n-1)；
另外一种选择是第一次跳2级，此时跳法数目等于后面剩下的n-2级台阶的跳法数目，即为f(n-2)。
因此n级台阶时的不同跳法的总数f(n)=f(n-1)+f(n-2)。
'''
def ClimbStairs1(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n>=3:
        return ClimbStairs1(n-1)+ClimbStairs1(n-2)
    else:
        print('error')
        return
#解法二
'''
解法一用的递归的方法有许多重复计算的工作，事实上，我们可以从后往前推，一步步利用之前计算的结果递推。
初始化时，dp[0]=dp[1]=1，然后递推计算即可：dp[n] = dp[n-1] + dp[n-2]。
'''
def ClimbStairs2(n):
    dp=[1,2]
    for _ in range(3,n+1):
        temp=dp[0]+dp[1]
        dp.pop(0)
        dp.append(temp)
    return dp[-1]
if __name__ == '__main__':
    print(ClimbStairs1(10))
    print(ClimbStairs2(10))