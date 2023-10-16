#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:35:11 2023

This is a program to calculate earning compound interest

P = Principal amount(initial investment)
r = annual nominal interst rate (as a decimal)
n = number of times the interest is compounded per year
t = number of years
A = final mount

\


@author: ruyonga
"""
from sys import exit

p = input("How much do you want to invest?\n")
if p.isdigit():
    p = float(p)
    print("principal is: ", p)
else:
    print("Invalid principal amount entered, restart the program")
    exit()


r = input("At what annual rate? ex. 10 NOT 10% \n")
if r.isdigit():
    r = float(r)/100
    print("Interest  is: ",  r)
else:
    print("Invalid entry entered, please enter number")

t = input("For how many years would you like to invest? \n")


if t.isdigit():
    t = int(t)
    print("investing period: ", t)
else:
    print("Invalid value entered, please enter number")

n = input("Enter the number of compounding per year? \n")


if n.isdigit():
    n = int(n)
    print("Compounding period: ", n)
else:
    print("Invalid value entered, please enter number")


print("principal", p, "interest", r, "period", t, "number of times", n)

#BODMAS
compounding = n * t
print("compounding nt:", compounding)
rate = r / n
print("calculated rate r/n:", rate)


step_1  = (1 + rate)
print("step (1 + rate)", step_1)

step_2 = pow(step_1, compounding)

print("step 2 step_2 ^ nt", step_2)

final_amount = p * step_2

print("You will have", str(round(final_amount, 2)), "after", n, "years")
