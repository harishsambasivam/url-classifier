from sklearn.linear_model import LogisticRegression
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error



df= pd.read_csv(r'C:\Users\imhar\Documents\dataset.csv')
columnsTitles = ["having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","on_mouseover","Iframe","Page_Rank"]
result=df['Result']
features=df.reindex(columns=columnsTitles)
# print(features.head())
# print(features.columns)
train_features, test_features, train_labels, test_labels = train_test_split(features, result, test_size = 0.01,random_state = 5)
#create logistic regression object
clf_lr = LogisticRegression(random_state=5)
#Train the model using training data 
clf_lr=clf_lr.fit(train_features,train_labels)

#Test the model using testing data
predictions = clf_lr.predict(test_features)

print("f1 score is ",f1_score(test_labels,predictions,average='weighted'))
print("matthews correlation coefficient is ",matthews_corrcoef(test_labels,predictions))

#secondary metric,we should not consider accuracy score because the classes are imbalanced.
print("Accuracy score is ",accuracy_score(test_labels,predictions))
