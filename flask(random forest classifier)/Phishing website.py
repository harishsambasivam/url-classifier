#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from mlxtend.preprocessing import minmax_scaling
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Import Dataset

df= pd.read_csv('C:/Users/dell/Downloads/phishing-website-dataset/dataset.csv')
df.head()


# In[3]:


# select the IP_address column
goal = df.having_IPhaving_IP_Address
scaled_data = minmax_scaling(goal, columns = [0])

# plot the original & scaled data together to compare
fig, ax=plt.subplots(1,2)
sns.distplot(df.having_IPhaving_IP_Address, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")


# In[4]:


a=len(df[df.Result==0])
b=len(df[df.Result==-1])
c=len(df[df.Result==1])
print(a,"times 0 repeated in Result")
print(b,"times -1 repeated in Result")
print(c,"times 1 repeated in Result")


# In[25]:


df.info()
df.describe()


# In[23]:


sns.pairplot(df)


# In[5]:


sns.countplot(df['Result'])


# In[6]:


result=df['Result']
features=df.drop(['Result'],axis=1)


# In[7]:


for i in features.columns:
    plt.title("%s"%i)
    plt.figure(figsize=(10,6))
    sns.countplot(df[i],hue=df['Result'])


# In[9]:


print(df.corr())
sns.heatmap(df.corr(),annot=True)


# In[27]:


features=df.drop('Result',axis=1).values 
result=df['Result'].values
print(features)


# In[28]:


from sklearn.model_selection import train_test_split

# Split the 'features' and 'result' data into training and testing sets
train_features, test_features, train_features, test_labels = train_test_split(features, 
                                                    result, 
                                                    test_size = 0.2, 
                                                    random_state = 5)


# In[29]:


#Randon Forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_features, train_features)
melb_preds = forest_model.predict(test_features)
print(mean_absolute_error(test_labels, melb_preds))


# In[30]:


#import Evaluation metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

#create logistic regression object
clf_lr = LogisticRegression(random_state=5)
#Train the model using training data 
clf_lr=clf_lr.fit(train_features,train_labels)

#Test the model using testing data
predictions = clf_lr.predict(test_features)

print("f1 score is ",f1_score(y_test,predictions,average='weighted'))
print("matthews correlation coefficient is ",matthews_corrcoef(test_labels,predictions))

#secondary metric,we should not consider accuracy score because the classes are imbalanced.
print("Accuracy score is ",accuracy_score(test_labels,predictions))


# In[31]:


#Decission Trees
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(criterion='entropy') # function to measure the quality of split 
tree.fit(train_features,train_features)
score = cross_val_score(tree, features,result, cv= 10) #
print(score)
print(score.mean())
y_pred = tree.predict(test_features)


# In[41]:


#KNN classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_predict, cross_val_score
k =1
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(train_features, train_features)
y_pred = knn.predict(test_features)
print(metrics.accuracy_score(test_labels, y_pred))
f1 = metrics.f1_score(features,result,average="weighted")
print(f1)


# In[42]:


#Navies Bias
from sklearn.naive_bayes import MultinomialNB

#create Naive Bayes object
model=MultinomialNB(alpha=1.0)

#Train the model using training data 
model.fit(train_features,train_features)
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
 
#Test the model using testing data
predictions = model.predict(test_features)
from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(test_labels,predictions)
sns.heatmap(cm,annot=True)
print("matthews correlation coefficient is ",matthews_corrcoef(test_labels,predictions))

#secondary metric,we should not consider accuracy score because the classes are imbalanced.

print('****************************************************************************************')
print("The accuracy of your Naive bayes on testing data is: ",100.0 *accuracy_score(test_labels,predictions))
print('****************************************************************************************')


# In[ ]:




