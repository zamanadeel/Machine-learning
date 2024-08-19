#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# In[6]:


# load the data tips from sns
df = pd.read_excel(r"C:\Users\dell\OneDrive\Desktop\DATAR1.xlsx")
# X mean Crude Oil Price and Y means LNG price extracted from X
df.head()


# In[7]:


sns.scatterplot(x='X', y='Y', data=df)


# In[8]:


# split the data into X and y
X = df[['X']]
# scalar = MinMaxScaler()
# X = scalar.fit_transform(X)
y = df['Y']


# In[9]:


# split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# In[10]:


# call the model
model = LinearRegression()


# In[11]:


# train the model
model.fit(X_train, y_train)


# In[12]:


# take out model intercept and slop, make an equation
print(model.intercept_)
print(model.coef_)
print('y = ', model.intercept_, '+', model.coef_, '* X')


# In[19]:


model.predict([[82.23]])


# In[17]:


# predict
y_pred = model.predict(X_test)


# In[14]:


# evaluate the model
print('MSE = ', mean_squared_error(y_test, y_pred))
print('R2 = ', r2_score(y_test, y_pred))
print('RMSE = ', np.sqrt(mean_squared_error(y_test, y_pred)))


# In[15]:


# plot the model and data
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.show()

