#!/usr/bin/env python
# coding: utf-8

# In[2]:


#To sort lexicographically by row or column index,use the sort_index method,
#which retuens a new sorted objcet
import pandas as pd
obj=pd.Series(range(4),index=['d','a','b','c'])
obj.sort_index()


# In[4]:


#With a DataFrame,you can sort by index on either axis
import numpy as np
frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
frame.sort_index()


# In[5]:


frame.sort_index(axis=1)


# In[6]:


#The data is sorted in ascending order by default,but can be sorted in descending order too
frame.sort_index(axis=1,ascending=False)


# In[7]:


#To sort aseries by values,use its sort_values method
obj=pd.Series([4,7,-3,2])
obj.sort_values()


# In[8]:


#Any missing values are sorted to the end of the series by defualt
obj=pd.Series([4,np.nan,7,np.nan,-3,2])
obj.sort_values()


# In[10]:


#We can use the data in one or more columns as the sort keys
#To do so,pass one or more column names to the  by option of sort_values
frame=pd.DataFrame({'a':[0,1,0,1],'b':[4,7,-3,2]})
frame


# In[12]:


frame.sort_values(by='b')


# In[13]:


#To sort by multiple columns,pass a list of names
frame.sort_values(by=['a','b'])


# In[14]:


#Ranking assigns ranks from one through the number of valid data points in an array
#By default rank breaks ties by assigning each group the mean rank
obj=pd.Series([7,-5,7,4,2,0,4])
obj.rank()


# In[15]:


#Ranks can also be assigned according to the order in which they are observed in the data
obj.rank(method='first')


# In[17]:


#rank in descending order
#assign tie values the maximum rank in the group
obj.rank(ascending=False,method='max')


# In[18]:


#DataFrane can compute ranks over the rows or the columns
frame=pd.DataFrame({'a':[0,1,0,1],'b':[4.3,7,-3,2],'c':[-2,5,8,-2.5]})
frame


# In[19]:


frame.rank(axis='columns')


# In[ ]:




