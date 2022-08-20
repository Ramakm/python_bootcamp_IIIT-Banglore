# **Python to make border 1's and Inside elements 0's**

import numpy as np

n = int(input("Enter the size of n: "))
    
border_array = np.ones((n,n), dtype = int)  #Making all elements in the ND array as 1's

border_array[1:-1, 1:-1] = 0 #making inside elements other than border as 0's

print(border_array)