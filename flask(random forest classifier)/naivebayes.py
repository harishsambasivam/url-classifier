#Navies Bias
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

columnsTitles = ["having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","on_mouseover","Iframe","Page_Rank","Result"
  ]
df= pd.read_csv(r'C:\Users\imhar\Documents\dataset.csv')


features=df.reindex(columns=columnsTitles)
xScaler = scaler.fit_transform(features)
result = features.iloc[:, : 1]
  # print(features.head())
  # print(features.columns)
train_features, test_features, train_labels, test_labels = train_test_split(features, 
                                                      result, 
                                                      test_size = 0.01, 
                                                      random_state = 5)
print(train_features,train_labels)
# #create Naive Bayes object
# model=MultinomialNB(alpha=1.0)

# #Train the model using training data 
# model.fit(train_features,train_labels)

 
# #Test the model using testing data
# predictions = model.predict(test_features)
# cm=confusion_matrix(test_labels,predictions)
# # sns.heatmap(cm,annot=True)
# print("matthews correlation coefficient is ",matthews_corrcoef(test_labels,predictions))


# print("The accuracy of your Naive bayes on testing data is: ",100.0 *accuracy_score(test_labels,predictions))
