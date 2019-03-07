#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:28:49 2019

@author: sparsh
"""

def add (a,b):
    return a+b;
def sub (a,b):
    return a-b;
def multiply (a,b):
    return a*b;
def div (a,b):
    return a/b;   
def choose():
    return int(input()); 


# print("1. Addition");
# print("2. Subtraction");
# print("3. Multiplication");
# print("4. Division");
# print("5. Exit");
# choice = choose();
# if (choice>=1 and choice<=4):
#     print("Enter two numbers: ");
#     num1 = int(input());
#     num2 = int(input());
#     if choice == 1:
#     	res = add(num1,num2);
#     	print("Result = ", res);
#     elif choice == 2:
#     	res = subt(num1,num2);1
#     	print("Result = ", res);
#     elif choice == 3:
#     	res = multip(num1,num2);
#     	print("Result = ", res);
#     else:
#     	res = div(num1,num2);
#     	print("Result = ", res);
# elif choice == 5:
#     exit();
# else:
#     print("Wrong input..!!");