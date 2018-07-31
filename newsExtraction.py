import requests
import pandas as pd
import json
import re

import urllib3
from bs4 import BeautifulSoup as bs

# url_actor2 = ('https://newsapi.oactor1/v2/everything?sources=the-hindu&q=actor2&from=2017-09-14&to=2017-12-14&apiKey=898565eccada4edda31b8781680ffe79')
# response_actor2 = requests.get(url_actor2)
# actor2 = json.loads(response_actor2.text)

# url_actor1 = ('https://newsapi.oactor1/v2/everything?sources=the-hindu&apiKey=898565eccada4edda31b8781680ffe79')
# response_actor1 = requests.get(url_actor1)
# actor1 = json.loads(response_actor1.text)

# #temp = json.dumps(parsed, indent=4, sort_keys=True)

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='898565eccada4edda31b8781680ffe79')

actor1 = newsapi.get_everything(q='rahul gandhi',sources='the-times-of-india',from_parameter='2017-9-14',to='2017-9-15')

actor2 = newsapi.get_everything(q='narendra modi',sources='the-times-of-india',from_parameter='2017-9-14',to='2017-9-15')

list_actor1 = []
list_actor2 = []
for i in range(0,len(actor1['articles'])):
    list_actor1.append([actor1['articles'][i]['publishedAt'], actor1['articles'][i]['title'], actor1['articles'][i]['url'], actor1['articles'][i]['description']])

for i in range(0,len(actor2['articles'])):
    list_actor2.append([actor2['articles'][i]['publishedAt'], actor2['articles'][i]['title'], actor2['articles'][i]['url'], actor2['articles'][i]['description']])


df_actor1 = pd.DataFrame(list_actor1, columns = ['publishedAt','title','url','description'])
df_actor2 = pd.DataFrame(list_actor2, columns = ['publishedAt','title','url','description'])


# http = urllib3.Poolist_actor2anager()
# link = 'https://timesofindia.indiatimes.com/india/pm-actor2-in-davos-to-attend-world-economic-forum/liveblog/62603731.cms'
# r = http.request('GET', link)
# soup = bs(r.data,'html.parser')


# data = soup.find_all( "div", class_='artText')
# #data2 = data.find_all('a')
# # if(data == False):
# # 	print('0')
# # else:
# # 	print('1')
# # print(len(data))
# # for i in range(0,len(t.strip())):
# #     if(t.strip()[i] =='\n'):
# # #len(t.strip().split())

# # p = " ".join(t.split())
# # print(p)


actor1_id = 1
for i in range(0,df_actor1.shape[0]):
    if (df_actor1.iloc[i]['url'][:21] == 'https://economictimes'):
        http = urllib3.PoolManager()
        link = df_actor1.iloc[i]['url']
        date = df_actor1.iloc[i]['publishedAt']
        request = http.request('GET', link)
        soup = bs(request.data,'html.parser')
        data = soup.find_all( "div", class_=('artText'))
        if(len(data) == 0):
            continue
        else:
            textFromData = data[0].get_text()

            cleanData = " ".join(textFromData.split())
            
            file = open('/Users/AR/Desktop/naturesCall/TOI_Data/actor1/'+str(date[:10])+'_actor1_'+str(actor1_id)+'.txt','w') 
            actor1_id = actor1_id+1
            file.write(cleanData)
            file.close()
    
    if (df_actor1.iloc[i]['url'][:20] == 'https://timesofindia'):
        http = urllib3.PoolManager()
        link = df_actor1.iloc[i]['url']
        date = df_actor1.iloc[i]['publishedAt']

        request = http.request('GET', link)
        soup = bs(request.data,'html.parser')
        data = soup.find_all( "div", class_=('Normal'))
        if(len(data) == 0):
            continue
        else:
            textFromData = data[0].get_text()

            cleanData = " ".join(textFromData.split())
            
            file = open('/Users/AR/Desktop/naturesCall/TOI_Data/actor1/'+str(date[:10])+'_actor1_'+str(actor1_id)+'.txt','w') 
            actor1_id = actor1_id+1
            file.write(cleanData)
            file.close()
            
actor2_id = 1           
for i in range(0,df_actor2.shape[0]):
    if (df_actor2.iloc[i]['url'][:21] == 'https://economictimes'):
        http = urllib3.PoolManager()
        link = df_actor2.iloc[i]['url']
        date = df_actor2.iloc[i]['publishedAt']

        request = http.request('GET', link)
        soup = bs(request.data,'html.parser')
        data = soup.find_all( "div", class_=('artText'))
        if(len(data) == 0):
            continue
        else:
            textFromData = data[0].get_text()

            cleanData = " ".join(textFromData.split())
         
            file = open('/Users/AR/Desktop/naturesCall/TOI_Data/actor2/'+str(date[:10])+'_actor2_'+str(actor2_id)+'.txt','w') 
            actor2_id = actor2_id+1
            file.write(cleanData)
            file.close()
    
    if (df_actor2.iloc[i]['url'][:20] == 'https://timesofindia'):
        http = urllib3.PoolManager()
        link = df_actor2.iloc[i]['url']
        date = df_actor2.iloc[i]['publishedAt']
   
        request = http.request('GET', link)
        soup = bs(request.data,'html.parser')
        data = soup.find_all( "div", class_=('Normal'))
        if(len(data) == 0):
            continue
        else:
            textFromData = data[0].get_text()

            cleanData = " ".join(textFromData.split())
            
            file = open('/Users/AR/Desktop/naturesCall/TOI_Data/actor2/'+str(date[:10])+'_actor2_'+str(actor2_id)+'.txt','w') 
            actor2_id = actor2_id+1
            file.write(cleanData)
            file.close()  
