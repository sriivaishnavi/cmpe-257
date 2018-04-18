
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df = pd.read_csv("Downloads/Irisdata.csv")
print(df)


# In[2]:


print("Variance of sepal length, width, petal length and width")
print(df.var())


# In[3]:


print("Median of sepal length, width, petal length and width")
print(df.median())


# In[5]:


print("Displaying the frequency of each value of sepal length")
pd.crosstab(index = df["sepal length"], columns = "count")


# In[6]:


print("displaying the histogram of Sepal length")
import matplotlib.pyplot as plt


# In[8]:


plt.hist(df['sepal length'], histtype = 'bar', facecolor = 'green',bins = (0,4.5,5.5,6.5,7.5,8.5))
plt.title("histogram for sepal length")
plt.axis([4,8.5,0,90])
plt.show()


# In[9]:


print(df.median())


# In[13]:


plt.plot(df['sepal width'], color = 'red')
plt.show();


# In[17]:


x_axis = ['sepal length', 'sepal width','petal length','petal width']
y_axis = [df['sepal length'].mean(), df['sepal width'].mean(), df['petal length'].mean(),df['petal width'].mean()]
plt.title('bar chart for mean') 
plt.bar(x_axis,y_axis, color = 'blue')
plt.show()

