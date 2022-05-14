#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')




# In[9]:


dataset = pd.read_csv('Ecommerce Customers.csv')


# In[10]:


dataset.head(10)


# In[15]:


dataset.info()


# In[ ]:





# In[ ]:





# In[14]:


sns.heatmap(dataset.corr(), annot = false)


# In[13]:


dataset.columns


# In[17]:


ax = sns.heatmap(Email, cmap="ylGnBu")


# In[ ]:




