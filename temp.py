# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pi=3.14
r=1.1
r=r**2
area=pi*r
print("Area of circle with radius 1.1 is ",area)
    

files={"java":"java",
       "js":"javascript",
       "py":"python",
       "txt":"document"
       }
x=input("Enter filename- ")
x=x.split(".")
x=x[1]
print("filename- ",x)
print("extension- ",files[x])

