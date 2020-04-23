#!/usr/bin/env python
# coding: utf-8

# In[1]:

# created in Jupyter
# need to add git to keep datafile current
# the following modules are prerequisites 

import pandas as pd
from matplotlib import pyplot as plt
import shutil


# In[2]:


shutil.copyfile('c:\\_SourceControl\\covid-19-data\\us-states.csv', 'us-states.csv')
US_data = pd.read_csv('us-states.csv')


# In[3]:


print('Compare your state to one other.')
yourstate = input('What is your state?    ')
state = input('Compare to which state?     ')
MY_data = US_data[US_data.state == yourstate]
ST_data = US_data[US_data.state == state]
plt.plot(MY_data.date, MY_data.cases)
plt.plot(ST_data.date, ST_data.cases)
plt.legend([yourstate, state])
plt.xticks([])
plt.xlabel('Date')
plt.ylabel('Cases')
plt.show()


# In[ ]:




