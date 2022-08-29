#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=input('Enter a number')


# In[2]:


print(a)


# In[3]:


type(a)


# In[4]:


b=int(a)
type(b)


# In[5]:


c=float(a)
type(c)


# In[6]:


list1=[1,2,3,4,5]
print(list1)


# In[7]:


fruits=[2,'apples',4,'mangoes']
print(fruits)


# In[8]:


count(fruits)


# In[9]:


print(count(fruits))


# In[10]:


apple=fruits.count('apple')
print(apple)


# In[11]:


fruits.count('apples')


# In[12]:


fruits.count(2)


# In[13]:


list2=[1,2,3,4,2,5,3,5,2,6,1,4,6]
list2.count(3)


# In[14]:


list2.pop()


# In[15]:


print(list2)


# In[16]:


list2.remove(3)


# In[17]:


print(list2)


# In[18]:


list2.sort()
print(list2)


# In[19]:


list3=[1,2,'a',5,'r','s',8]
list3.sort()
print(list3)


# In[20]:


list3.reverse()
print(list3)


# In[21]:


list3.index(5)


# In[22]:


list3.extend(4)
print(list3)


# In[23]:


print(list2)


# In[24]:


list2.extend(6)
print(list2)


# In[25]:


list2.extend(list3)
pr


# In[26]:


print(list2)


# In[27]:


list2.append('Hello World')
print(list2)


# In[28]:


list2.insert(1,'Aliyaan')
print(list2)


# In[29]:


list2.insert('APple')
print(list2)


# In[30]:


list2.clear()


# In[31]:


print(list2)


# In[32]:


print(list3)


# In[33]:


copylist3=list3.copy()


# In[34]:


print(copylist3)


# In[ ]:




