# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:18:39 2020

@author: Md. Yeasin Ali
"""

"""  Calculator
  --------------------
"""
# Create functions for addition, substraction,multiplication,division,and average
def addition():
    print("Addition")
    n=float(input("Enter the number: "))
    t=0 # Total number enter
    add=0
    while n!=0:
        add=add+n
        t+=1
        n=float(input("Enter the another number (0 to calculate): "))
    return [add,t]

def subtraction():
    print("Subtraction")
    n=float(input("Enter the number: "))
    sub=n
    t=0
    while n!=0:
        sub=sub-0
        n=float(input("Enter the another number (0 to calculate): "))
        sub=sub-n
        t+=1
    return [sub,t]

def multiplication():
    print("Multiplication")
    n=float(input("Enter the number: "))
    t=0
    multiple=1
    while n!=0:
        multiple=multiple*n
        t+=1
        n=float(input("Enter the another number (0 to calculate): "))
    return [multiple,t]

def division ():
    print("Division")
    n=float(input("Enter the number: "))
    t=0
    div=n
    while n!=0:
        div=div/1
        n=float(input("Enter the another number (0 to calculate): "))
        div=div/n
        t+=1
    return [div,t]

def average():
    add=addition()
    sum=add[0]
    n=add[1]
    aver=sum/n
    return [aver,n]


while True:
    print("My first python program")
    print("Simple calculation in python by Md. Yeasin Ali(Ayaan)")
    print("Enter 'a' for addition")
    print("Enter 's' for subtraction")
    print("Enter 'm' for multiplication")
    print("Enter 'd' for division")
    print("Enter 'v' for average")
    print("Enter 'q' for quite")
    
    c=input("What do you want? Please enter the key character: ")
    if c.lower()!="q":
        if c.lower()=="a":
            li=addition()
            print("Ans =",li[0], " total inputs:",li[1])
            
        elif c.lower()=="s":
            li=subtraction()
            print("Ans=",li[0]," total inputs:",li[1])
            
        elif c.lower()=="m":
            li=multiplication()
            print("Ans=",li[0]," total inputs:",li[1])
            
        elif c.lower()=="d":
            li=division()
            print("Ans=",li[0]," total inputs:",li[1])
            
        elif c.lower()=="v":
            li=average()
            print("Ans=",li[0]," total inputs:",li[1])
            
        else:
            print("Sorry! Invilid character")
            
    else:
        break
    
    again=input("Do you want to perform another calculation? (Enter Yes/No): ")
    if again.lower()=="yes":
        continue
    else:
        break


        