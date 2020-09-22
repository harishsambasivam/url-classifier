import re
import requests
from bs4 import BeautifulSoup
from mechanize import Browser
import OpenSSL
import ssl, socket

url = "https://emergencetherapies.co.uk///AjIFOQsmnfawvDz/df/fr/?i=6436236"
r = requests.get(url)         
soup = BeautifulSoup(r.text, "html.parser")
browser = Browser()
validLink = re.compile("^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")

ipaddressRegEx = re.compile("^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?|^((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/.*)?$")


redirectionRegex = re.compile("([^:]\/{2,3})")

subdomainRegex = re.compile("(?:http[s]*\:\/\/)*(.*?)\.(?=[^\/]*\..{2,5})")

dict = {"having_IP_Address":1,"URL_Length":1,"Shortining_Service":1,"having_At_Symbol":1,"double_slash_redirecting":1,"Prefix_Suffix":1,"having_Sub_Domain":1,"Favicon":1,"port":1,"HTTPS_token":1,"Request_URL":1,"URL_of_Anchor":1,"metaData":1,"SFH":1,"Submitting_to_email":1,"on_mouseover":1,"Iframe":1,"Page_Rank":1} 

def split(word): 
    return [char for char in word] 
letterArray = split(url)
length = len(letterArray) 
# "having_At_Symbol"
for letter in letterArray: 
    if(letter == '@') : 
        print("found @ symbol")
        dict["having_At_Symbol"] = -1 
        break

# having ip address
if ipaddressRegEx.match(url):
        print("found a match")
        dict["having_IP_Address"] = -1

# having subdomain
subdomaintest = subdomainRegex.match(url)
if subdomaintest:
    if subdomaintest.group(1) != "www":
        print("found a subdomain match")
        dict["having_Sub_Domain"] = -1



#length of the url
if length >= 52:
    dict["URL_Length"] = -1
elif length >25 and length < 52:
    dict["URL_Length"] = 0

# doubleslash redirection regex
redirectiontest = redirectionRegex.search(url)
if redirectiontest:
        print("found a match")
        dict["double_slash_redirecting"] = -1
        print(redirectiontest.groups())


#find url shortener
browser.open("http://checkshorturl.com/expand.php")
browser.select_form(nr=0)
browser['u'] = url
response = browser.submit()
content = response.read()
shortenedLink = BeautifulSoup(content,"html.parser")
# for td in soup.find_all('td'):
#         print(td)
if len(shortenedLink.find_all('td')) > 0:
    # print(soup.find_all('td')[1].get_text())
        dict["Shortining_Service"] = -1



# "having_hyphen_Symbol"
for letter in letterArray: 
    if(letter == '-') : 
        print("found - symbol")
        dict["Prefix_Suffix"] = -1 
        break

#ssl certificate


#favicon
linkTagWithFavicon = soup.find('link',{"rel" : "icon"})
if linkTagWithFavicon:
    linkhref = linkTagWithFavicon['href']
    redirectiontest = validLink.match(linkhref)
    if redirectiontest:      
        dict["Favicon"] = -1

#http port
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((url, 80))
    s.shutdown(2)
except:
    dict["port"] = -1



#https inside domain name
splittedURL = url.split("//")
domainname = splittedURL[1]
if 'https' in domainname :
        dict["HTTPS_token"] = -1



#multimedia are loaded from same site
srcArr = []
count = 0
images = soup.find_all('img')
try:
    for img in images:
        print(img['src'])
        srcArr.append(img['src']) 
except:
    print('Error')


videos = soup.find_all('video')
try:
    for video in videos:
        srcArr.append(video['src'])
except:
    print('Error')

iframes = soup.find_all('iframe')
try:
    for i in iframes:
        srcArr.append(i['src']) 
except:
    audio = soup.find_all('audio')
    for a in audio:
        srcArr.append(a['src'])  

for src in srcArr:
    if validLink.match(src):
        count+=1

if count >= (len(srcArr)/2):
    dict["Request_URL"] = -1
    # print("phish")
# print(count,len(srcArr))


#URL_of_Anchor
anchor = soup.find_all('a')
anchorArray = []
try:
    for a in anchor:
            anchorArray.append(a['href'])
            continue
except:
    print('No href in anchor')
# print(anchorArray)
anchorArrayhreflen = len(anchorArray)
anchorArraylen = len(anchor)
if anchorArraylen != anchorArrayhreflen:
    dict["URL_of_Anchor"] = -1



#metaData
metadata = soup.find_all('meta')
if len(metadata) == 0:
    print("no meta data available")
    dict['metaData'] = -1
elif len(metadata) < 3:
    dict['metaData'] = 0


#SFH
formactionArray = []
forms = soup.find_all('form')
try:
    for f in forms:
        formactionArray.append(f['action'])
except:
    print('error in sfh')

if len(formactionArray) < len(forms):
    dict["SFH"] = -1
print(formactionArray)

#mailto
mailtoRegex = re.compile('\'mailto\:([^">]+)\'([^>]*)')
for action in formactionArray:
     mailtotest = validLink.match(action)
     if mailtotest:
         dict["Submitting_to_email"] = -1


#on_mouseover

for a in anchor:
    try:
       if a['onMouseOver']:
           dict["on_mouseover"] = -1
    except:
        1+1



#iframes

for i in iframes:
    if i['frameborder'] == 0:
        dict['Iframe'] = -1

#age of domain
# whois = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_Aa2UmTMsJRPJMCHI11Ur0nkbYxhwi&domainName="+url) 
# print(whois)
# soupwhois = BeautifulSoup(whois.text, "html.parser")
# # print(soupwhois)
# print(soupwhois.find('createddatenormalized'))
# print(soupwhois.find('createddate'))


browser.open("https://checkpagerank.net/index.php")
browser.select_form(nr=1)
browser['name'] = url
prresponse = browser.submit()
prcontent = prresponse.read()
pagerank = BeautifulSoup(prcontent,"html.parser")
# print(pagerank)
pageRankofurl = pagerank.find_all('h2')[2].find_all('b')[1].text.split('/')[0]
print("#############")
if len(pageRankofurl) > 0:
    if float(pageRankofurl) < 1:
        dict["Page_Rank"] = -1
else:
    dict["Page_Rank"] = -1

datatoPredict = list(dict.values())
print(type(datatoPredict))
print(len(dict.values()))


import numpy as np
import pandas as pd
from scipy import stats #
# from mlxtend.preprocessing import minmax_scaling
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.model_selection import train_test_split

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


forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_features, train_labels)
predictions = forest_model.predict(test_features)
print("%%%%%%%%%%%%%%%%%%%%")
print(forest_model.predict([datatoPredict]))
print("%%%%%%%%%%%%%%%%%%%%")

print(mean_absolute_error(test_labels, predictions))
print(100-mean_absolute_error(test_labels, predictions))



