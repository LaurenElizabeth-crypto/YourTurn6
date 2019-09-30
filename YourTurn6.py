#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


bins = [0,80,100]
status_name = ['Fail', 'Pass']
df ['status'] = pd.cut (df['grade'], bins, labels=status_name)
df


# In[3]:


bins = [0,80,100]
status_name = ['Fail', 'Pass']
df ['status'] = pd.cut (df['grade'], bins, labels=status_name)
pd.value_counts(df['status'])


# In[ ]:




