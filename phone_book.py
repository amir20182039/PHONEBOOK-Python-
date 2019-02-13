#!/usr/bin/python -tt
#/****************************************************#
# Author  : Amir Elmallah                             #
# Version : v01                                       #
# Date    : 8 Feb 2019                                #
#*****************************************************#
#DESCRIPTION                                          #
#-----------                                          #
# This file defines the PHONEBOOK  BY PYTHON          #
# Save it to File Database                            #
#*****************************************************#
#                                                     #
import sys,os

def PhoneBook(a,args):
  # +++your code here+++
  dict={}
  spdict={}
  flagnotfound=0;
  if a == "a":
   f=open("phone_Book.txt",'r')
    list=f.readlines()
    f.close()
    for line in list:
     if args[0] in line:
       list.remove(line)
   if len(args)== 4:
    dict[args[0]]=spdict
    spdict['num']=args[1]
    spdict['mail']=args[2]
    spdict['work']=args[3]
    f=open("phone_Book.txt",'a')
    f.write(str(dict)+"\n")
    f.close()
   else:
    print "you have to enter with the add the 4 arguments"   
  if a == "d":
    f=open("phone_Book.txt",'r')
    for line in f:
     print line
    f.close()
  if a == "c":
    dict.clear();
    f=open("phone_Book.txt",'w')
    f.write(" ")
    f.close()
  if a == "r":
    f=open("phone_Book.txt",'r')
    list=f.readlines()
    f.close()
    k=open('phone_Book.txt','w')
    for line in list:
     if args[0] in line:
       list.remove(line)
       flagnotfound=1;
    for line in list:      
       k.write(line)
    if flagnotfound == 0:
       print "The name is not found in the Dictionary"
    k.close()

def main():
  if len(sys.argv) < 2 or sys.argv[1]!='a' and  sys.argv[1]!='d' and  sys.argv[1]!='c' and  sys.argv[1]!='r':
    print '----------->a add \n----------> d display\n---------->c  clear all\n--------->r remove\n'
    print ' a (add) and r(remove) need at least one argument  ' 
    sys.exit(1)
  '''
  Inside the main function, check on the passed option and call the proper function.
  If the passed option is unknown print: 'unknown option: ' + option 
  and then exit with failure.
  
'''
  PhoneBook(sys.argv[1],sys.argv[2:])
  
if __name__ == '__main__':
  main()  
