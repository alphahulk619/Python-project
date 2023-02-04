#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style


# In[3]:


df= pd.read_csv("airline_delay_causes_Feb2020_2.csv")


# In[4]:


df.head()


# # Data Cleaning

# In[5]:


df.isnull().sum()


# In[6]:


df[df['arr_del15'].isnull()]


# In[7]:


df=df.drop(labels=[568,1709], axis=0)


# In[8]:


df.isnull().sum()


# # Total number of flights

# In[9]:


## arr_flights represents total number of arriving flights
Total_number_of_flights = df[' arr_flights'].sum()
print(Total_number_of_flights)


# In[10]:


## Total number of flights = 574266


# # Total number of delayed flights

# In[11]:


## arr_del15 represents number of flights delayed
total_delayed_flights = df['arr_del15'].sum()
total_delayed_flights


# In[13]:


## Total number of delayed flights = 84616


# # Total delayed time

# In[14]:


## arr_delay represents delay in terms of time
total_delayed_time=df['arr_delay'].sum()
print(total_delayed_time)


# In[15]:


Total_delay_time_in_min= (total_delayed_time/60)
print(Total_delay_time_in_min)


# # Airport with largest number of delayed flights

# In[16]:


## Using groupby() function 
airport_with_largest_delayed_flights=df.groupby("airport").sum()["arr_del15"]


# In[17]:


airport_with_largest_delayed_flights.head()


# In[18]:


pd.set_option('display.max_columns', 23)
pd.set_option('display.max_rows', 1769)


# In[19]:


airport_with_largest_delayed_flights


# In[20]:


## using max() fucntion
airport_with_largest_delayed_flights.max()


# In[21]:


## ATL (Atlanta, GA: Hartsfield-Jackson Atlanta International) is the airport with most number of delayed flights


# # Coordinates (from Part A) of the airport with highest delayed time

# In[22]:


airport_with_highest_delayed_time=df.groupby("airport").sum()["arr_delay"]


# In[23]:


print(airport_with_highest_delayed_time)


# In[24]:


airport_with_highest_delayed_time.max()


# In[25]:


## ATL is the airport with highest delayed time
## now using 1st csv file to find its coordinates 
## ATL is in state Georgia (GA)


# In[26]:


df2=pd.read_csv("airports_1.csv")
df2.head()


# In[27]:


df2[df2['city']=='Atlanta']


# In[28]:


###hence from the above table we can see the Coordinates of ATL which is lat-33.640444,long--84.426944


# # Airport in Texas which has the largest number of delayed flights

# In[29]:


## Selecting Airport in Texas


# In[30]:


df_tx= df[df['airport_name'].str.contains('TX')]


# In[31]:


## creating a list 
lst_tx_delay=list(df_tx['arr_del15'])


# In[32]:


print(max(lst_tx_delay))


# In[33]:


# Corresponding airport in Texas
tx_delay= df_tx[df_tx['arr_del15']==1812.0]
print(tx_delay['airport_name'])


# # Pie chart

# In[46]:


sum_of_columns=df.sum(axis=0)
print(sum_of_columns)


# In[47]:


On_time_flights=489650
Air_carrier_delay=33891
Weather_delay=5653
nas_delay=22979
security_delay=127
Aircraft_arriving_late=34331
cancelled=5133
diverted=1057


# In[48]:


labels=['on-time flights','Air Carrier delay','weather delay','NAS delay','Security Delay','Aircraft Arriving Late','Cancelled','Diverted']
quantity=[489650,33891,5653,22979,127,34331,5133,1057]

plt.pie(quantity,autopct='%0.01f%%',shadow=False,explode=[0,0,0.2,0.1,0.5,0.1,0,0.3])
plt.legend(labels,loc='upper right',bbox_to_anchor = (2,0.75))
plt.title('Airport Delay Analysis')
plt.show()


# In[ ]:





# In[ ]:




