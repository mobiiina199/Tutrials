#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#import plotly.graph_objects as go


# In[5]:


i = 0 
while i<=10:
    print(i)
    i += 1


# In[6]:





# In[9]:


lastnumber = 6
for row in range(1, lastnumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")


# ### n(n+1)/2

# In[19]:


sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)


# ### n!

# In[23]:


Factorial = 1
n = int(input("please enter number:"))
for i in range(1, n+1):
    Factorial = Factorial*i
print('\n sum is:', Factorial)


# ### n(n-1)/2

# In[24]:


sum2 = 1
n = int(input("please enter number:"))
for i in range(1, n+1):
    sum2 -= i
print('\n sum is:', sum2)


# In[37]:


sum3 = 2
for i in range (2, 11, 1):
    print(sum3)
    sum3 = 2*i


# In[41]:


list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if i > 150:
        break
    if i%5 == 0:
        print(i)


# In[50]:


num = int(input("please enter number:"))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits are: ", count)


# In[57]:


k = 5
for i in range(0, 6):
    for j in range(k-i, 0, -1):
        print(j, end=' ')
    print()


# In[71]:


list1 = [10, 20, 30, 40, 50]
start = len(list1) - 1
step = -1
stop = -1
for i in range(start, stop, step):
    print(list1[i])


# In[73]:


np.flip(list1)


# In[81]:


n = 54
np.flip(list1, -1)


# In[105]:


num = 45
num2=0
while num > 0:
    num1 = num % 10
    num2= (num2*10) + num1
    num = num // 10
print("Revered Number ", num2)


# In[104]:


num1


# In[94]:


45%10


# In[113]:


num = int(input("please enter number:"))
for i in range(1, num+1):
    print(i**3)
    


# In[114]:


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# In[ ]:




