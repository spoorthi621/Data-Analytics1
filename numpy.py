#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Create a ID array
import numpy as np
arr1=np.array([1,2,3])
print(arr1)


# In[2]:


#2.accessing elements from the array
arr1[2]


# In[5]:


#change an element from the array
arr1[2]=5
arr1


# In[6]:


arr1


# In[8]:


#3.Craete a 2D array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[9]:


#Check the shape of array
print("The shape is 2rows and 3 columns:",arr2.shape)


# In[10]:


#4.accessing elements from the array
print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[11]:


#5.Array of type string
arr3=np.array(['India','China','USA','Mexico'])
print(arr3)


# In[12]:


arr3[1]


# In[14]:


#6.Array of evenly spaced values within a specified interval
arr=np.arange(0,20,2)
print(arr)


# In[40]:


#Array of evenly spaced number in a specified interval
arr=np.linspace(0,10,20)
print(arr)


# In[37]:


#7.Array of random values between 0 and 1 in  a given shape
arr=np.random.rand(10)
print(arr)
print('\n')
arr=np.random.rand(3,4)
print(arr)


# In[23]:


#8.Array of constatnt values in a given shape
print(np.full((4,6),10))


# In[18]:


#9.Create an  array by repetition
#repeat each element of an array by a specified number of times
arr=[0,1,2]
print(np.tile(arr,3))


# In[41]:


#10.Create and identity matrix
identity_matrix=np.eye(4)
print(identity_matrix)


# In[20]:


#11.create a 5*5 2D array for random numbers between 0 and 1
arr=np.random.rand(5,5)
print(arr)


# In[21]:


#12.Sum an array along the column
print(np.sum(arr,axis=0))


# In[22]:


#13.Sum an array along the row
print(np.sum(arr,axis=1))


# In[25]:


#14.Calculate the mean,median,sd, and variance
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[26]:


#15.Sort an array along the row using the sort() function
arr=np.random.rand(5,5)
print(arr)


# In[27]:


#sorting along the row
print(np.sort(arr,axis=1))


# In[28]:


#16.Append elements to an array using the appand() fuction
arr=np.array([4,5,6,7])


# In[29]:


arr1=np.append(arr,8)
arr1


# In[30]:


arr2=np.append(arr,[9,10,11])
print(arr2)


# In[31]:


#17.Delete mutiple elements in an array
arr2=np.array([4,5,6,7,8,9,10,11])
print(arr2)
print('\n')
arr5=np.delete(arr2,[1,4])
print(arr5)


# In[32]:


#18.Combine and split an array
arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[35]:


#Combine the array items by column
cat=np.concatenate((arr1,arr2),axis=0)
print(cat)


# In[34]:


#combine array items by row
cat=np.concatenate((arr1,arr2),axis=1)
print(cat)


# In[ ]:




