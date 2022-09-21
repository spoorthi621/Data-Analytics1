#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
from scipy import stats
from scipy.stats import f
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[10]:


a=[4,3,2]
b=[2,4,6]
c=[2,1,3]


# In[11]:


stats.f_oneway(a,b,c)


# In[12]:


data=pd.read_excel('oneway.xlsx')


# In[13]:


data


# In[15]:


data_new=pd.melt(data.reset_index(),id_vars=['index'],value_vars=['Black Board','Case Presentation','PPT'])
data_new.columns=['index','Treatments','value']


# In[16]:


data_new


# In[17]:


model=ols('value~C(Treatments)',data=data_new).fit()
anova_table=sm.stats.anova_lm(model,typ=1)
anova_table


# In[ ]:




