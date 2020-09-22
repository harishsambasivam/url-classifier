from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.tree import DecisionTreeClassifier

columnsTitles = ["having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","on_mouseover","Iframe","Page_Rank"
  ]
df= pd.read_csv(r'C:\Users\imhar\Documents\dataset.csv')



result=df['Result']
features=df.reindex(columns=columnsTitles)
  # print(features.head())
  # print(features.columns)
train_features, test_features, train_labels, test_labels = train_test_split(features, 
                                                      result, 
                                                      test_size = 0.01, 
                                                      random_state = 5)

tree = DecisionTreeClassifier(criterion='entropy') # function to measure the quality of split 
tree.fit(train_features,train_labels)
score = cross_val_score(tree, features,result, cv= 10) #
print(score)
print(score.mean())
y_pred = tree.predict(test_features)