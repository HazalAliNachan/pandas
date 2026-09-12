#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# # Series
# 
# 
# 

# In[3]:


marks = pd.Series([85, 90, 76, 95])

print(marks)


# In[4]:


print(marks[1])


# # DataFrame

# In[6]:


data = {
    "Name": ["Rahul", "Anu", "Raj"],
    "Age": [20, 21, 19],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df)


# # CREATING DATAFRAME

# In[14]:


# From Dictionary
data = {
    "Name":["Hazal","Ali"],
    "Age":[20,19]
}
df = pd.DataFrame(data)


# In[15]:


df


# In[16]:


# From List
data = [
    ["Hazal",20],
    ["Ali",19]
]
df = pd.DataFrame(data,columns=["Name","Age"])
df


# In[ ]:


# df = pd.read_csv(" ")


# In[18]:


data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    
    "Name": [
        "Aarav", "Diya", "Rohan", "Ananya", "Karan",
        "Meera", "Aditya", "Sneha", "Rahul", "Priya"
    ],
    
    "Age": [19, 20, 19, 20, 21, 19, 20, 21, 19, 20],
    
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    
    "Department": [
        "AIML", "CSE", "AIML", "ISE", "CSE",
        "AIML", "ISE", "CSE", "AIML", "ISE"
    ],
    
    "Math": [85, 78, 92, 67, 74, 88, 59, 95, 81, 73],
    
    "Python": [90, 85, 95, 72, 68, 91, 65, 93, 79, 77],
    
    "AI": [88, 82, 94, 70, 76, 90, 62, 97, 85, 71],
    
    "Attendance": [92, 88, 96, 75, 82, 94, 70, 98, 89, 80],
    
    "Projects": [3, 2, 4, 1, 2, 3, 1, 5, 2, 2],
    
    "Placement": [
        "Yes", "Yes", "Yes", "No", "No",
        "Yes", "No", "Yes", "Yes", "No"
    ]
}
df = pd.DataFrame(data)


# In[21]:


df


# In[22]:


df.head()


# In[23]:


df.tail()


# In[33]:


df.shape


# In[34]:


df.columns


# In[35]:


df.info()


# In[36]:


df.describe()


# In[37]:


df["Age"] # returns a series


# In[39]:


df[["Age","Math"]] # return a dataframe


# In[41]:


# Selecting Rows
# Location by label
df.loc[0]


# In[42]:


df.loc[0:2] # 0 to 2 both are included 


# In[43]:


df.loc[0:2,["Math","Age"]]


# In[ ]:


# iloc location by integer position
# follows normal python slicing so 3 is excluded


# In[46]:


df.iloc[0:3]


# In[47]:


df.iloc[0,3]


# In[48]:


df.iloc[1,8]


# In[49]:


df[df["Age"]>20]


# In[53]:


df[(df["Age"] > 20) & (df["Math"] > 80)]


# In[58]:


df.sort_values("Age",ascending = True) # sort in ascending


# In[59]:


df.sort_values("Age",ascending = False) # sort in descending


# In[60]:


df["Age"] = df["Age"] + 1


# In[61]:


df


# In[62]:


df.drop("Projects",axis =1,inplace=True) # inplace=True-->permanently delete


# In[63]:


df


# In[65]:


# df.isnull()
df.isnull().sum()


# In[66]:


df.dropna() #Removes rows containing missing values


# In[ ]:


# df["Age"].fillna(20)
# df["Age"].fillna(df["Age"].mean())  ---> IMPUTATION
# Missing Age
     # ↓
# calculate average Age
     # ↓
# put average in missing location


# In[67]:


df.duplicated().sum()


# In[68]:


df.drop_duplicates()


# In[69]:


df.dtypes


# In[71]:


df["Age"] = df["Age"].astype(float)


# In[72]:


df


# In[75]:


df["Age"] = pd.to_numeric(df["Age"]) #Changing Data Type


# In[76]:


df


# In[77]:


df["Name"] = df["Name"].str.strip()


# In[78]:


df


# In[79]:


df["Name"] = df["Name"].str.lower()
df.head()


# In[80]:


df["Name"] = df["Name"].str.upper()
df.head()


# In[81]:


df["Math"].value_counts()


# In[82]:


df["Age"].unique()


# In[83]:


df["Age"].nunique()


# In[84]:


df.groupby("Gender")["Math"].mean()


# In[85]:


df.groupby("Gender")["Math"].agg(["max","min","mean"])


# In[90]:


df1 = pd.Series(["a", "b"])
df2 = pd.Series(["c", "d"])

pd.concat([df1, df2])


# In[93]:


df.rename(columns={"Age":"Student_Age"})

