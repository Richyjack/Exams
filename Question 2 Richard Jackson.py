#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
plt.rc("font", size=14)
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style="whitegrid", color_codes=True)


# In[8]:


dataset = pd.read_csv('advertising.csv')


# In[3]:


dataset.head(10)


# In[4]:


data['education'].unique()


# In[5]:


data['y'].value_Counts()


# In[11]:


dataset.describe()


# In[18]:


dataset.columns


# In[12]:


dataset.info()


# In[19]:


sns.pairplot(dataset)


# In[24]:


get_ipython().run_cell_magic('timeit(dataset', '%)', '')


# In[26]:


sns.heatmap(dataset.corr(), annot = True)


# In[51]:


###dataset = plt


# In[52]:


###dataset.show()


# In[53]:


sns.displot(dataset['Age'])


# In[54]:


data = np.random.randn(50, 20)


# In[ ]:





# In[46]:


import numpy as np; np.random.seed(1)
import seaborn as sns; sns.set_theme()
uniform_data = np.random.rand(10, 10)
ax = sns.heatmap(uniform_data)


# In[ ]:





# In[ ]:




