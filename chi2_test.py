#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


acad=pd.read_excel('acad.xlsx')


# In[5]:


acad


# In[6]:


obs=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
obs


# In[7]:


from scipy.stats import chi2_contingency


# In[8]:


chi2,p,dof,tbl=chi2_contingency(obs)


# In[9]:


chi2


# In[10]:


p


# In[11]:


dof


# In[12]:


tbl


# In[ ]:




