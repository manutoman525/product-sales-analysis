#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import seaborn as sn
df = pd.read_csv('Diwali Sales Data.csv',encoding = 'unicode escape')
df.head()


# In[32]:


df.info()


# In[33]:


df1 = df.drop(columns = ['Status','unnamed1'])


# In[34]:


pd.isnull(df1).sum()


# In[37]:


df2 = df1.dropna()


# In[38]:


pd.isnull(df2).sum()


# In[39]:


df2.head()


# In[66]:


sales = df.groupby('Gender',as_index=False)['Orders'].sum().sort_values(by='Gender',ascending = False)


# In[67]:


sales.reset_index(drop=True)
sales.head()


# In[71]:


sn.barplot(data = sales,y='Orders',x='Gender')


# Females have ordered most in the sales
# 

# In[72]:


sales1 = df.groupby('Age Group',as_index=False)['Orders'].sum().sort_values(by = 'Orders',ascending = False)
sales1.head()


# In[78]:


sn.barplot(data = sales1,x= 'Age Group',y = 'Orders')


# people of age group between 26-35 have ordered most
# 

# In[79]:


sales2 = df.groupby('Gender',as_index = False)['Amount'].sum()


# In[80]:


sn.barplot(data = sales2,x = 'Gender',y = 'Amount')


# Females have generated revenue of >70,000,000 RS and  Males have generated revenue of >30,000,000

# In[86]:


sales3 = df.groupby('State',as_index = False)['Orders'].sum(10)
sn.set(rc ={'figure.figsize':(20,5)})
sn.barplot(data = sales3,x = 'State',y = 'Orders')


# people of UP have ordered most products

# In[ ]:




