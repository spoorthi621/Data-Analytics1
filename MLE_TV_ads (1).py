#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy.optimize import minimize
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


tb1=pd.read_excel('regcar.xlsx')
tb1


#  

# In[4]:


import statsmodels.api as sm
x=tb1['TV Ads']
y=tb1['car Sold']
x2=sm.add_constant(x)
mod1=sm.OLS(y,x2)
mod2=mod1.fit()
print(mod2.summary())


# In[5]:


e=mod2.resid


# In[6]:


e


# In[7]:


np.std(e)


# In[9]:


def lik(parameters):
    m=parameters[0]
    b=parameters[1]
    sigma=parameters[2]
    for i in np.arange(0,len(x)):
        y_exp=m*x+b
        l=(len(x)/2*np.log(2*np.pi)+len(x)/2*np.log(sigma**2)+1/(2*sigma**2)*sum((y-y_exp)**2))
        return l


# In[10]:


lik_model=minimize(lik,np.array([5,5,5]),method='Nelder-Mead')


# In[11]:


lik_model.x


# In[12]:


plt.scatter(x,y)
plt.plot(x,lik_model['x'][0]*x+lik_model['x'][1])
plt.show()


# In[ ]:




