#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:


#load the dataset
data1=pd.read_csv('E:\download-python\gapminder-FiveYearData.csv')


# In[4]:


#display dataset
data1


# In[5]:


#displaythe head of the dataset(shows only 5rows)
data1.head()


# In[6]:


#get number of rows and columns
print(data1.shape)


# In[7]:


#get column names
data1.columns


# In[8]:


#get the dtype of each column
data1.dtypes


# In[9]:


#get more information about data
data1.info()


# In[10]:


#looking at columns,rows and cells
#get the country column and save it in a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[11]:


#show the last 5 observations
country_data.tail()


# In[12]:


#looking at country,continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[13]:


subset.tail()


# In[14]:


#Analytical summary of the dataset
data1.describe(include='all')


# In[15]:


#Histogram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[17]:


#relation ship between catagorical and continious variable
sns.boxplot(x="year",y="lifeExp",data=data1)


# In[19]:


#drop irrelevant columns
data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[22]:


#Renaming the column name
data1=data1.rename(columns={"country" : "Countries"})
data1.head(5)


# In[25]:


#Rows containing duplicate data
duplicate_rows=data1[data1.duplicated()]
print('Number of duplicate rows:',duplicate_rows.shape)


# In[26]:


#count the rows before moving the data
data1.count()


# In[ ]:




