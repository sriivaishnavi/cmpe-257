
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df = pd.read_csv("E:/ml/Irisdata.csv")
print(df)


# In[2]:



varianceresult = df.var()
print(varianceresult)


# In[3]:


print("mean")
meanresult = np.mean(df['sl'])
print(meanresult)


# In[5]:


import matplotlib.pyplot as plt
print("median")
print("sl"," ", np.median(df['sl']))
print("sw"," ",np.median(df['sw']) )
print("pl"," ", np.median(df['pl']))
print("pw"," ", np.median(df['pw']))
print("Scatter plots")
plt.scatter(df['sl'], df['pl'],df['sw'],df['pw'])
plt.show()
print("Bar Chart")
plt.bar(df['sl'], df['pl'],df['sw'],df['pw'])
plt.show()
print("Line Graph")
plt.plot(df['sl'], df['pl'],df['sw'],df['pw'])
plt.show()

