'''Description:
A class of students attempt an exam in two parts: ‘Aptitude’ and ‘Physics'. The marks of all the students are stored as a list of tuples, and each student’s marks (in Aptitude and Physics) are stored in each tuple. Your task is to write a Python program to sort the list of tuples in decreasing order of the Physics scores of the students.
Note - Marks of both the subjects are ranged between 1-100, and no two students have scored the same marks in Physics.
---------------------------------------------------------------------------------------------------
Input - List of tuples

Output - List of tuples
---------------------------------------------------------------------------------------------------
Sample Input - [(45,77), (88,87), (67,98), (33,31)]
In (45,77), which is the first element in the list, 45 and 77 are the scores of a student in aptitude and physics respectively.
Sample Output - [ (67,98), (88,87), (45,77),(33,31)]
'''
import ast
input_tup = ast.literal_eval(input())

sorted_tuple = sorted(input_tup,reverse=True,key= lambda x: x[1])

print(sorted_tuple)