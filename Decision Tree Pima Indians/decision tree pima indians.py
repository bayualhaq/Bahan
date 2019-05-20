#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image  
from sklearn import metrics
import pydotplus
import numpy as np


# In[4]:


data = pd.read_csv('PimaIndians.csv')
data.head()


# In[5]:


data.info()


# In[6]:


zero_not_accepted = ['pregnant','glucose','diastolic','triceps','insulin','bmi','diabetes','age']
# for col in zero_not_accepted:
#     for i in data[col]:
#         if i==0:
#             colSum = sum(data[col])
#             meanCol=colSum/len(data[col])
#             data[col]=meanCol

for col in zero_not_accepted:
    data[col]= data[col].replace(0,np.NaN)
    mean = int(data[col].mean(skipna=True))
    data[col] = data[col].replace(np.NaN,mean)


# In[8]:


X = data.iloc[:,0:8]
y = data.iloc[:,8]

X = data[['pregnant','glucose','diastolic','triceps','insulin','bmi','diabetes','age']]
y = data['test']

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=0)


# In[13]:


# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[14]:


feature_cols = ['pregnant','glucose','diastolic','triceps','insulin','bmi','diabetes','age']
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['positif','negatif'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())


# In[ ]:




