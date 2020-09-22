from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np



columnsTitles = ["having_IPhaving_IP_Address","URLURL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting","Prefix_Suffix","having_Sub_Domain","Favicon","port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email","on_mouseover","Iframe","Page_Rank"
  ]
df= pd.read_csv(r'C:\Users\imhar\Documents\dataset.csv')



result=df['Result']
features=df.reindex(columns=columnsTitles)
  # print(features.head())
  # print(features.columns)
train_features, test_features, train_labels, test_labels = train_test_split(features, 
                                                      result, 
                                                      test_size = 0.25, 
                                                      random_state = 30)

forest_model = RandomForestRegressor(n_estimators= 1000, random_state=100)
forest_model.fit(train_features, train_labels)
predictions = forest_model.predict(test_features)
print("Mean absolute error:"+mean_absolute_error(test_labels, predictions))
# print(100-mean_absolute_error(test_labels, predictions))
# print(accuracy_score(test_labels,predictions))
# Calculate mean absolute percentage error (MAPE)
errors = abs(predictions - test_labels)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy), '%.')