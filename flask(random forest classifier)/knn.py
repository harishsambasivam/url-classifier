from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

columnsTitles = ["having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","on_mouseover","Iframe","Page_Rank"
  ]
df= pd.read_csv(r'C:\Users\imhar\Documents\dataset.csv')



result=df['Result']
features=df.reindex(columns=columnsTitles)
print(len(features.columns))
  # print(features.head())
  # print(features.columns)
xScaler = scaler.fit_transform(features)
train_features, test_features, train_labels, test_labels = train_test_split(xScaler, 
                                                      result, 
                                                      test_size = 0.01, 
                                                      random_state = 5)


k =1
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(train_features, train_labels)
y_pred = knn.predict(test_features)
print(metrics.accuracy_score(test_labels, y_pred))
f1 = metrics.f1_score(features,result,average="weighted")
print(f1)