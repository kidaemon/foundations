
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get('https://finance.yahoo.com/industries')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


stocks = doc.find_all('tr')[2:]
len(stocks)


# In[4]:


list_of_stocks = []

for stock in stocks:
    stock_dic = {}
    symbol = stock.find('a')
    symbol_link = stock.find('a').get('href')
    industry = stock.find(class_='data-col1')
    industry_link = stock.find(class_='data-col1').find('a').get('href')
    price = stock.find(class_='data-col2')
    change = stock.find(class_='data-col3')
    percent_change = stock.find(class_='data-col4')
    if symbol:
        stock_dic['Symbol'] = symbol.text
    if symbol_link:
        stock_dic['Symbol Link'] = 'https://finance.yahoo.com'+symbol_link
    if industry:
        stock_dic['Industry'] = industry.text
    if industry_link:
        stock_dic['Industry Link'] = 'https://finance.yahoo.com'+industry_link
    if price:
        stock_dic['Price'] = price.text
    if change:
        stock_dic['Change'] = change.text
    if percent_change:
        stock_dic['% Change'] = percent_change.text
    list_of_stocks.append(stock_dic)

list_of_stocks


# In[5]:


df = pd.DataFrame(list_of_stocks)
df


# In[6]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%m-%d-%-I%p")


# In[7]:


date_string


# In[8]:


df.to_csv('briefing-'+date_string+'.csv', index=False)


# In[9]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox32923414644541fca4e0f5aae3e2f4e3.mailgun.org/messages",
        auth=("api", "XXXXXX"),
        files=[("attachment", open('briefing-'+date_string+'.csv'))],
        data={"from": "Kazuhiro Kida <mailgun@sandbox32923414644541fca4e0f5aae3e2f4e3.mailgun.org>",
              "to": "kazuhiro.kida@nex.nikkei.com",
              "subject": "Here is your 6PM briefing",
              "text": df}) 
response.text

