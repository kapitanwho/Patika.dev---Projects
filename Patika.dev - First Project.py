#!/usr/bin/env python
# coding: utf-8

# # Patika.dev 1. Soru

# In[51]:


c = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


# In[63]:


l = []
def flatten(x,y):
    for item in x:
        if type(item) is list:
            flatten(item,y)
        else:
            y.append(item)


# In[64]:


flatten(c,l)


# In[65]:


l


# # Patika.dev 2.Soru

# In[317]:


a = [[1, 2], [3, 4], [5, 6, 7]]


# In[339]:


i = -1
def ters(m):
    while i < 3:
        a[i].reverse()
        i += 1


# In[341]:


print(a)

