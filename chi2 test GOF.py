#!/usr/bin/env python
# coding: utf-8

# In[2]:


import scipy
from scipy.stats import chi2
from scipy.stats import poisson


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_excel('P_distribution.xlsx')
data


# In[5]:


Observed_Freq=data['Frequency']


# In[6]:


Observed_Freq


# In[7]:


total_arrival=600
total_time_period=100
mu=total_arrival/total_time_period


# In[8]:


mu


# In[9]:


Expected_Freq=[]
for i in range(len(Observed_Freq)):
    E_Freq=100*poisson.pmf(i,mu)
    Expected_Freq.append(E_Freq)


# In[10]:


Expected_Freq


# In[11]:


Expected_Freq_round_off=[round(elem,2)for elem in Expected_Freq]
Expected_Freq_round_off


# In[15]:


df=pd.DataFrame(list(zip(Observed_Freq,Expected_Freq_round_off)),columns=['Observed Frequency','Expected Frequency'])
df


# In[17]:


obs_freq=[5,10,14,20,12,12,9,8,10]
expected_freq=[6.20,8.92,13.39,16.06,16.06,13.77,10.33,6.88,8.39]


# In[18]:


scipy.stats.chisquare(obs_freq,expected_freq)


# In[ ]:




