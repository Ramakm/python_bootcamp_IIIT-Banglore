#!/usr/bin/env python
# coding: utf-8

# # upgrad-bootcamp-week2-practice
# 
# Use the "Run" button to execute the code.

# In[ ]:


get_ipython().system('pip install jovian --upgrade --quiet')


# In[ ]:


import jovian


# In[ ]:


# Execute this to save new versions of the notebook
jovian.commit(project="upgrad-bootcamp-week-2-assignments")


# In[ ]:


# MCQs Questions  


# In[1]:


# What is the output of the following?

s = 'a$b@c@d'
print(s.split('@','$'))

#Ans = Error


# # What is the code to print the element ‘banana’?
# 
# fruits = ['apple', 'mango', ['grapes', 'papaya'], ('banana', 'pomegranate')]
# 
# #Ans = fruits[3][0]
# 

# # What will the output of the following code be?
# 
# num_1=[9,4,2,7]
# num_2=[8,3,6,1]
# print(sorted(num_1))
# print(num_1)
# print(num_2.sort())
# print(num_2)

# In[3]:


#Find the output of the following code.

l = ['paris','india','china','london']
print(tuple(l+['sri lanka']))


# In[4]:


#What is the output of the following code?

var=(5)
print(type(var))


# #What is the output of the code given below?
# 
# tup=([1,3,5],"abcd",(2,4),6)
# tup[0][2]=7
# print(tup)

# #What will the output of the following code be?
# 
# a= {1,2,4,5}
# b= {5,6,7,8}
# print(a-b)

# # What will the output of the following code be?
# 
# s= {3,4,5}
# s*2
# 
# #Ans = Error 

# # What is the output of the following code?
# 
# numbers= {1,0,6,1,4,0,7}
# print(len(numbers))

# # What will the output of the following Python code be?
# 
# dict= {'ab':12,'cd':34,'ef':56}
# print(dict[1])
# 
# #Ans = Error

# # What will the output of the following code be?  
# 
# marks= {'John':45,'Alex':60}
# print(marks.keys())
#  

# # What is the output of the following code?
# 
# d = {"Python":40, "R":45}
# "Python" in d

# # What will the output of the following code be?
# 
# input_dict= {1:"one",2:"two",3:"three"}
# for i in input_dict:
#   print(i)

# # Find the output of the following code snippet.
# 
# input_str="I love programming in python"
# count=0
# l=['a','e','i','o','u']
# for i in input_str.lower():
#   if i in l:
#   	count=count+1
# print(count)

# In[ ]:


#  Practice Question 1


# In[ ]:





# '''Description
# Suppose you want to know the total score of the Indian cricket team in a given match. To do so, your task is to find the sum of all the scores of the Indian team players. The scores are provided as a list, with each element as an individual score of the players. Also, there is a condition that if the number of elements in the list is more than 11, then it is an invalid input and the output should be -1.
# 
# --------------------------------------------------------------------------------------------
# 
# Input - List
# 
# Output - An integer
# --------------------------------------------------------------------------------------------
# 
# Sample Input : [11, 13, 101, 14, 33, 141]
# 
# Sample Output : 313
# ---------------------------------------------------------------------------------------------
#     
# Sample Input : [11, 13, 101, 14, 33, 141, 12, 144, 54, 67, 8, 11]
# 
# Sample Output : -1
# ---------------------------------------------------------------------------------------------
# 
# Sample Input : [100, 80, 30, 10, 0, 1, 2, 0]
# 
# Sample Output : 223 '''
# 
# 

# In[ ]:


import ast,sys
input_str=sys.stdin.readline()
input_list=ast.literal_eval(input_str)
sum =0
if len(input_list)<11:
    for i in input_list:
      sum = sum+ i
    print(sum)

else:
    print(-1)


# '''Length of list elements
# Description
# Given a list of strings, write a program to find the number of strings whose length is greater than or equal to K, where K is a positive integer.
# 
# Input - List of strings and an integer
# 
# ﻿Output - Integer
# 
# --------------------------------------------------------------------------------
# 
# Sample Input :
# 
# [Mumbai, Hyderabad, Calicut, Chennai]
# 
#   9
# 
# Sample Output: 1
# 
# -------------------------------------------------------------------------------
# Sample Input :
# 
# [Datascience, Data Analyst, Programmer, Manager]
# 
#   8
# 
# Sample Output : 3'''

# In[ ]:


#Take input here using ast sys
import ast,sys
input_str=sys.stdin.readline()
input_list=ast.literal_eval(input_str)
K = int(input())
count = 0
for elements in input_list:
    if len(elements)>=K:
        count = count +1
print(count)


# In[ ]:


'''Increment list elements
Description
Given a list of strings, increment the value of the numeric strings by 'k’. 



Hint: The function isdigit() may be useful here.



---------------------------------------------------------------------------------------------

Input - A list in the first line and an integer in the second line

Output - A list

---------------------------------------------------------------------------------------------

Sample Input :

['Python', '123', 'Data']

  4


Sample Output : ['Python', '127', 'Data']

---------------------------------------------------------------------------------------------

Sample Input :

['upGrad', '1991', 'Mumbai']

  0

Sample Output : ['upGrad', '1991', 'Mumbai']

---------------------------------------------------------------------------------------------

Sample Input :

['Data Science', '100', '10']

  10



Sample Output : ['Data Science', '110', '20']'''


# In[ ]:


#Input has been taken for you
import ast
input_list = ast.literal_eval(input())
K = int(input())
list1 = []
for element in input_list:
    if element.isdigit():
        element = int(element) + K
        new_element = str(element)
        list1.append(new_element)
    else:
        list1.append(element)
print(list1)


# '''Slicing a list
# Description
# Given a list of strings and an integer K, write a python code to print all the elements from the K th position till the end of the list.
# 
# 
# 
# Note: Assume that K (a positive integer) will always be less than or equal to the length of the list
# 
# 
# Input - A list of strings in the first line and an integer in the second line of the input.
# 
# Output - A list
# 
# 
# 
# --------------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input :
# 
# ['Mumbai', 'Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']
# 
# 2
# 
# 
# 
# Sample Output : ['Delhi', 'Australia', 'Nigeria', 'USA', 'London', 'Canada']
# 
# 
# 
# --------------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input :
# 
# ['Chennai', 'Vizag', 'Austria', 'Germany', 'Japan']
# 
# 3
# 
# 
# 
# Sample Output : ['Austria', 'Germany', 'Japan']
# 
# Execution Time Limit
# 10 seconds'''

# In[ ]:


#read the input using the ast sys
import ast
input_list = ast.literal_eval(input())
K = int(input())
if K<= len(input_list):
    print(input_list[K-1:])


# In[ ]:


#  Practice Question 2


# In[ ]:





# '''Substring with maximum uppercase characters
# Description
# Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring. Check the sample inputs and outputs for a better understanding.
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# Input - String
# 
# Output - String
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - I lovE PRogrAMMING
# 
# Sample Output - 6
# 
# 
# 
# Explanation - AMMING is the largest substring with all characters in uppercase continuously 
# 
# 
# 
# -----------------------------------------------------------------------------------------------------
# 
# Sample Input - MuMbaI is in MAHArashTRA
# 
# Sample Output - 4
# 
# 
# 
# Explanation - MAHA is the largest substring with all characters in uppercase continuously.
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# Sample Input - India WOn the WOrLD CUP
# 
# Sample Output - 3
# 
# 
# 
# Explanation - CUP is the largest substring with all characters in uppercase continuously.
# 
# Execution Time Limit
# 10 seconds
# '''

# In[ ]:


# #Take input here

test_str = input()
upper = 0
max_upper = []

for i in test_str:
    if i.isupper():
        upper += 1 
        max_upper.append(upper)
    else:
        upper = 0
print(max(max_upper))


# '''Sorting list of tuples
# Description
# A class of students attempt an exam in two parts: ‘Aptitude’ and ‘Physics'. The marks of all the students are stored as a list of tuples, and each student’s marks (in Aptitude and Physics) are stored in each tuple. Your task is to write a Python program to sort the list of tuples in decreasing order of the Physics scores of the students.
# 
# 
# 
# Note - Marks of both the subjects are ranged between 1-100, and no two students have scored the same marks in Physics.
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# Input - List of tuples
# 
# Output - List of tuples
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - [(45,77), (88,87), (67,98), (33,31)]
# 
# 
# 
# In (45,77), which is the first element in the list, 45 and 77 are the scores of a student in aptitude and physics respectively.
# 
# 
# 
# Sample Output - [ (67,98), (88,87), (45,77),(33,31)]
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - [(45,23), (45,88), (45,98), (45,44)]
# 
# 
# 
# Sample Output - [ (45,98), (45,88), (45,44),(45,23)]
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - [(55,77), (34,90), (67,100), (90,0)]
# 
# 
# 
# Sample Output - [ (67,100), (34,90), (55,77),(90,0)]
# 
# Execution Time Limit
# 10 seconds'''

# In[ ]:


import ast
input_tup = ast.literal_eval(input())

sorted_tuple = sorted(input_tup,reverse=True,key= lambda x: x[1])

print(sorted_tuple)


# '''Divisibility check
# Description
# Given an integer ‘n’, your task is to write a Python code to find whether ‘n’ is divisible by all its digits or not. If they divide the number, then the number ‘n’ is a happy number. Otherwise, it is a sad number.
# 
# The number ‘n’ may be provided with commas. At first, you have to clean the number (by removing the commas involved) and then check whether the number is happy or sad.
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Input - String
# 
# Output - String
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# Sample Input - 2,128
# 
# Sample Output - Happy Number
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - 256
# 
# Sample Output - Sad Number
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# 
# 
# Sample Input - 1124
# 
# Sample Output - Happy Number
# 
# 
# 
# ---------------------------------------------------------------------------------------------------
# 
# Execution Time Limit
# 10 seconds'''

# In[ ]:


n = input()
x = n.replace(',','')
flag = True

for i in x:
    if int(i)!=0 and int(x)%int(i)==0:
        flag = True
    else:
        flag = False
        break
if flag:
    print('Happy Number')
else:
    print('Sad Number')


# In[ ]:


#  Practice Question 3 


# '''Updating the dictionary keys:
# 
# Description:
# 
# You are provided with a dictionary containing the names of different football clubs as keys and the name of the main player of the corresponding team as values. When the main player of a team retires, one of their teammates steps up to fill in their role as the main player.
# 
# You’re also provided with a list which contains the names of the football clubs for which the current main players are retiring and the names of the corresponding new main player. Your task is to update the values in the original dictionary with the names of the new main players.
# 
# -----------------------------------------------------------------------------------------------------
# 
# Input - The input consists of a dictionary with different football clubs' names and their main player. In the next line, you will be provided with a list of the new players who have taken up the main roles.
# 
# Output - Dictionary
# 
# ---------------------------------------------------------------------------------------------------
# 
# Sample Input :
# 
# {Barcelona:’Messi’ , ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Neymar’ }
# 
# [[‘Barcelona’, ‘Griezmann’], [‘PSG’, ‘Ramos’]]
# 
# Sample Output: {Barcelona:‘Griezmann’, ‘Real Madrid’: ‘Benzema’, ‘PSG’: ‘Ramos’}
# 
# --------------------------------------------------------------------------------------------------
# 
# Sample Input:
# 
# {Liverpool:’A’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }
# 
# [[Liverpool, ‘R’]]
# 
# Sample Output: {Liverpool:’R’, ‘Real Madrid’: ‘B’, ‘Chelsea’: ‘C’ }
# 
# ---------------------------------------------------------------------------------------------------
# 
# Sample Input :
# 
#  {Atletico Madrid : ’D’ , ‘Juventus’: ‘B’, ‘Chelsea’: ‘C’ }
# 
# [[‘Juventus’, ‘G’], [‘Chelsea’, ‘H’]]
# 
# Sample Output: {Atletico Madrid : ’D’, ‘Juventus’: ‘G’, ‘Chelsea’: ‘H’ }
# 
# Execution Time Limit
# 10 seconds'''

# In[ ]:


import ast
input_dict = ast.literal_eval(input())
input_list = ast.literal_eval(input())

def check_in_dict(d,l):
    for key in d:
        for element in l:
            if element[0] == key:
                d[key] = element[1]
            else:
                pass
    return d

print(check_in_dict(input_dict,input_list))


# '''List average:
# 
# Description:
# 
# Suppose you are working as a Marketing Lead in a company and you want to recruit new employees in your team (which already consists of 10 members) to carry out the company’s major project. You select the employees based on five parameters: A, B, C, D and E. The value of each parameter is represented on a scale of 1 to 10. The present average value of these parameters for your team is given to you in a list (in the same order). You recruit a person only if their scores do not reduce the average score of more than two parameters of your team. If they are recruited, print the output as ‘Selected’. If not, print the output as ‘Rejected’.
# --------------------------------------------------------------------------------------------------
# Input - Two lists, where the first list is the average scores of the team in the five parameters, and the second list is the scores of the new employee in all the five parameters. The parameter order is the same for both the lists, which is A, B, C, D and E.
# 
# Output - String
# --------------------------------------------------------------------------------------------------
# Sample Input - [‘8’, ‘4’, ‘6’, ‘9’, ‘7’]
# 
#   [‘1’, ‘1.1’, ‘1.2’, ‘1.2’, ‘2.3’]
# 
# Sample Output - Rejected
# --------------------------------------------------------------------------------------------------
# 
# Sample Input - [‘10’, ‘5’, ‘6’, ‘9’, ‘7’]
# 
#   [‘10’, ‘ 9.8’, ‘7.2’, ‘1.66’, ‘4.3’]
# 
# Sample Output - Selected
# 
# --------------------------------------------------------------------------------------------------
# 
# Sample Input - [‘8’, ‘5.66’, ‘6.5’, ‘10’, ‘10’]
# 
#   [‘7’, ‘ 10’, ‘6’, ‘7’, ‘9’]
# 
# Sample Output - Rejected
# 
# Execution Time Limit
# 10 seconds'''

# In[ ]:


import ast,sys
input_list1 = ast.literal_eval(input())
input_list2 = ast.literal_eval(input())
count = 0
for i,j in zip(input_list1, input_list2):
    if float(j)>float(i):
        count += 1
if count>=2:
    print("Selected")
else:
    print("Rejected")


# '''
# Merge dictionaries
# Description
# Write a python code to merge two dictionaries into a single dictionary.
# --------------------------------------------------------------------------------------------------
# Input: Two dictionaries, one in each line
# Output: A Dictionary
# --------------------------------------------------------------------------------------------------
# Sample Input :
# 
# {'a': 10, 'b': 8}
# 
# {'d': 6, 'c': 4}
# 
# Sample Output : {'c': 4, 'a': 10, 'b': 8, 'd': 6}
# 
# --------------------------------------------------------------------------------------------------
# Sample Input` :
# 
# {'a': 110, 'b': 88}
# 
# {'d': 62, 'c': 44}
# Sample Output : {'a': 110, 'b': 88, 'd': 62, 'c': 44}
# --------------------------------------------------------------------------------------------------
# Execution Time Limit
# 10 seconds'''

# In[ ]:


import ast,sys
input_dictionary1 = input()
convert_dictionary1 = ast.literal_eval(input_dictionary1)
input_dictionary2 = input()
convert_dictionary2 = ast.literal_eval(input_dictionary2)
# print({**convert_dictionary1, **convert_dictionary2})

convert_dictionary1.update(convert_dictionary2)
print(convert_dictionary1)


# In[ ]:





# In[ ]:





# In[ ]:




