#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(100,160,2)
print(arr)


# In[4]:


# access the individual array elements
print('First element')
print(arr[0])
print('Second element')
print(arr[1])
print('third element')
print(arr[2])
print('fifth element')
print(arr[4])


# In[5]:


# slicing of array indexes [start:stop:step]
arr[0:5:1]


# In[6]:


# updating array using slices 
arr[0:5] = 0
print(arr)


# In[12]:


# memory allocation view vs copy
arr2 = arr[4:10]
print(arr2)
arr2[:] = 1
print(arr2)


# In[13]:


print(arr)


# In[20]:


# copy function creating new numpy memory for array
arr3 = arr.copy()
print(arr3)


# In[21]:


print(arr3)
print(arr)

