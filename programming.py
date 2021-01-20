# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 01:42:46 2021

@author: USER
"""
from googlesearch import search 
  
# to search 
#query = "Which programming language to begin with"
  
#for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
   # print(j) 
def TopResult(query):
    result="Here are the best solutions for your query: \n\n"
    counter=1
    for j in search(query, tld="co.in", num=3, stop=3, pause=2): 
        result+=str(counter)
        result+=") "
        result+=j
        result+='\n\n'
        counter+=1
    return result
