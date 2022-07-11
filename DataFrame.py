#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing python library
import pandas as pd
import numpy as np


# In[2]:


#Dataframe will have its index assigned automatically,
#the columns are placed in sorted order
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
#using the jupyter notebook,pandas DataFrame objects will be displayed as a more browser friendly HTML table.
frame


# In[3]:


#head method selects only first 5 rows
frame.head()


# In[5]:


#specify a sequence of columns
pd.DataFrame(data,columns=['year','state','pop'])


# In[7]:


#If you pass a column that isnt contained in the dict,it will appear with msiig values in the result
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[8]:


frame2.columns


# In[9]:


#A column in a DataFrame can be retrieved as a series either by dict-like notation or by attribute
frame2['state']


# In[10]:


frame2.year


# In[11]:


#Rows can be retrived by position or name with the special loc attribute
frame2.loc['three']


# In[12]:


#columns can be modified by assignment
#'debt' column could be assigned a scalar value or an array of values
frame2['debt']=16.5
frame2


# In[14]:


frame2['debt']=np.arange(6.)
frame2


# In[16]:


#assign a series,its labels will be realigned exactly to the DataFrames index,inserting misiing values in any holes
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2


# In[17]:


#add a new column of boolean values where the state column equals 'OHIO'
frame2['eastern']=frame2.state=='Ohio'
frame2


# In[18]:


#The del method can then be used to remove this column 
del frame2['eastern']
frame2.columns


# In[19]:


#data is a nested dict of dicts
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3


# In[22]:


#transpose the dataframe
frame3.T


# In[23]:


#sorted to form the index in the result
pd.DataFrame(pop,index=[2001,2002,2003])


# In[25]:


#DataFrames index and columns have their nam attributes set
frame3.index.name='year';frame3.columns.name='state'
frame3


# In[26]:


#values attribute returns the data contained in the DataFrame as a two-dimensional nd array
frame3.values


# In[27]:


frame2.values


# In[ ]:




