#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-09-10 19:46:34
# @Author: Lao Jiangwei
# @Version : $Id$
import numpy as np

def MulMatrix(matrixA,matrixB):
    n,l1=matrixA.shape
    l2,m=matrixB.shape
    if l1!=l2:
        print('Two matrices cannot be multiplied')
        return
    else:
        l=l1
    matrixC=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            for k in range(l):
                matrixC[i,j]+=matrixA[i,k]*matrixB[k,j]
    return matrixC

if __name__ == '__main__':
    matrixA=np.random.randint(0,10,(3,6))
    matrixB=np.random.randint(0,10,(6,9))
    print('matrixA')
    print(matrixA)
    print('matrixB')
    print(matrixB)
    print('result')
    print(MulMatrix(matrixA,matrixB))