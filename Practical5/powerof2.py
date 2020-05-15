# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:01:39 2020

@author: 86133
"""
import random
x = random.randint(1,8192)
x1 = x
print(x,"is",sep=" ",end="")
for i in range(0,14):
    j = 13 - i
    if x > 2 **j:
        print("2**",j,sep=" ",end="") 
        print("+",end="")
        x = x - 2 ** j
    elif x == 2 ** j:
        print("2**",j,end="")
        x = x - 2 ** j