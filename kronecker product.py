#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:49:42 2023

@author: ruyonga

Given 2 a and b matrices the kronecker product is each element of matrix a *  elements in b

"""
import numpy as np

a1 = int(input("Enter elements of first matrix, first row a1\n"))
a2 = int(input("Enter elements of first matrix, first row a2\n"))
a3 = int(input("Enter elements of first matrix, second row a3\n"))
a4 = int(input("Enter elements of first matrix, second row a4\n"))

matrix_a = [[a1, a2], [a3, a4]]

print("Your matrix a pxq = {0} ".format(matrix_a))


b1 = int(input("Enter elements of second matrix, first row b1\n"))
b2 = int(input("Enter elements of second matrix, first row b2\n"))
b3 = int(input("Enter elements of second matrix, second row b3\n"))
b4 = int(input("Enter elements of second matrix, second row b4\n"))

matrix_b = [[b1, b2], [b3, b4]]

print("Your matrix b mxn = {0} \n".format(matrix_b))

print("Kronecker Matrix  for aXb  =  [[a1* b1..bn, a2 * b1..bn] , [a3 * b1..bn], [a4* b1..bn]]")


def do_raw_product(a, b):
    a1b1 = a[0][0] * b[0][0]
    a1b2 = a[0][0] * b[0][1]
    a1b3 = a[0][0] * b[1][0]
    a1b4 = a[0][0] * b[1][1]
    
    
    a2b1 = a[0][1] * b[0][0]
    a2b2 = a[0][1] * b[0][1]
    a2b3 = a[0][1] * b[1][0]
    a2b4 = a[0][1] * b[1][1]
    
    a3b1 = a[1][0] * b[0][0]
    a3b2 = a[1][0] * b[0][1]
    a3b3 = a[1][0] * b[1][0]
    a3b4 = a[1][0] * b[1][1]
    
    a4b1 = a[1][1] * b[0][0]
    a4b2 = a[1][1] * b[0][1]
    a4b3 = a[1][1] * b[1][0]
    a4b4 = a[1][1] * b[1][1]
    
    a1 = [a1b1, a1b2, a1b3, a1b4]
    a2 = [a2b1, a2b2, a2b3, a2b4]
    a3 = [a3b1, a3b2, a3b3, a3b4]
    a4 = [a4b1, a4b2, a4b3, a4b4]
    
    return [a1,a2,a3,a4]

print(np.matrix(do_raw_product(matrix_a, matrix_b)))

def do_simp_product(matrix_a ,matrix_b):

    f_matrix = []
    pdc = 0
    
    for (i, _) in enumerate(matrix_a):
        for (j, _) in enumerate(matrix_b):
            
         pdc = matrix_a[i][i] * matrix_b[j][j] 
         f_matrix.append(pdc)

    
    return  f_matrix

print("This is another attempt")
print(np.matrix(do_simp_product(matrix_a, matrix_b)))