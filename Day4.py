#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the pandas library for data manipulation and analysis
import pandas as pd


# In[4]:


# Load the insurance dataset and display the first 10 rows
df = pd.read_csv('insurance.csv')
df.head(10)


# In[3]:


# Check for missing values in the dataset
df.isnull().sum()


# In[8]:


# Import numpy, seaborn, and matplotlib for numerical operations and visualization
# Plot the distribution of insurance charges with a KDE curve
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['charges'],kde=True)


# In[9]:


# Apply Box-Cox transformation to the 'bmi' column to normalize the data
from scipy.stats import boxcox
df['bmi_boxcox'],_ = boxcox(df['bmi'] + 1)


# In[10]:


# Display the dataset with the new 'bmi_boxcox' column
df.head()


# In[11]:


# Create a new column 'log_charges' using logarithmic transformation of charges
# Then plot the distribution of the transformed charges
df['log_charges'] = np.log1p(df['charges'])
sns.histplot(df['log_charges'],kde=True)


# In[12]:


# Categorize BMI values into underweight, normal, overweight, and obese
df['bmi_cat'] = pd.cut(df['bmi'], bins =[0,18.5,25,30,100],labels=['under','normal','over','obese'])


# In[13]:


# Categorize age values into groups: young, adult, mature, senior
df['age_group'] = pd.cut(df['age'], bins =[17,30,45,60,100],labels=['young','adult','mature','senior'])


# In[15]:


# Create a new feature 'age_smoker' by multiplying age with smoker status
df['age_smoker'] = df['age'] * (df['smoker']=='yes')


# In[16]:


# Display the dataset with all the new columns
df.head()


# In[18]:


# Plot the distribution of log-transformed charges and Box-Cox transformed BMI
sns.histplot(df['log_charges'],kde=True)

sns.histplot(df['bmi_boxcox'],kde=True)             


# In[17]:


# Create a boxplot to compare insurance charges across different BMI categories
sns.boxplot(x='bmi_cat',y='charges',data=df)


# In[20]:


# Create a boxplot to compare insurance charges between smokers and non-smokers
sns.boxplot(x='smoker',y='charges', data=df)


# In[38]:


# Import pandas again for student-course dataset manipulation
import pandas as pd


# In[40]:


# Load the students dataset and display the first 5 rows
df_students = pd.read_csv('students.csv')
print(df_students.head())


# In[43]:


# Load the courses dataset and display the first 5 rows
df_courses = pd.read_csv('courses.csv')
print(df_courses.head())


# In[45]:


# Perform an INNER JOIN between students and courses on Course_ID
inner_join = pd.merge(df_students, df_courses, on='Course_ID',how="inner")
print("INNER JOIN Result:")
print(inner_join, "\n")


# In[48]:


# Perform an OUTER JOIN between students and courses on Course_ID
outer_join = pd.merge(df_students, df_courses, on='Course_ID',how="outer")
print("OUTER JOIN Result:")
print(outer_join, "\n")


# In[50]:


# Perform a LEFT JOIN between students and courses on Course_ID
left_join = pd.merge(df_students, df_courses, on='Course_ID',how="left")
print("LEFT JOIN Result:")
print(left_join, "\n")


# In[49]:


# Perform a RIGHT JOIN between students and courses on Course_ID
right_join = pd.merge(df_students, df_courses, on='Course_ID',how="right")
print("RIGHT JOIN Result:")
print(right_join, "\n")


# In[ ]:





# In[ ]:




