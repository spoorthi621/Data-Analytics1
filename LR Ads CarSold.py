#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[2]:


import matplotlib as mpl
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
from scipy import stats


# In[5]:


tbl=pd.read_excel('regr.xlsx')
tbl


# In[13]:


tbl.plot('TV Ads','car Sold',style='o')
plt.ylabel('car Sold')
plt.title('Sales In Several UK Region')
plt.show()


# In[14]:


t=tbl['TV Ads']
c=tbl['car Sold']


# In[17]:


import statsmodels.api as sm
t=sm.add_constant(t)
model1=sm.OLS(c,t)
result1=model1.fit()
print(result1.summary())


# In[ ]:




