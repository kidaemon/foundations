
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.get('https://api.darksky.net/forecast/XXXXXX/40.8075,-73.9626')


# In[3]:


data = response.json()


# In[4]:


TEMPERATURE = data['currently']['temperature']
TEMPERATURE


# In[5]:


SUMMARY = data['currently']['summary']
SUMMARY


# In[6]:


HIGH_TEMP = data['daily']['data'][0]['temperatureHigh']
HIGH_TEMP


# In[7]:


if HIGH_TEMP > 90:
    TEMP_FEELING = 'hot'
elif 80 <= HIGH_TEMP < 90:
    TEMP_FEELING = 'warm'
elif 70 <= HIGH_TEMP < 80:
    TEMP_FEELING = 'moderate'
else:
    TEMP_FEELING = 'cold'
TEMP_FEELING


# In[8]:


LOW_TEMP = data['daily']['data'][0]['temperatureLow']
LOW_TEMP


# In[12]:


if data['daily']['data'][0]['icon'] == 'rain':
    RAIN_WARNING = 'Bring your umbrella!'
else:
    RAIN_WARNING = ''
RAIN_WARNING


# In[13]:


weather = "Right now it is "+str(TEMPERATURE)+" degrees out and "+SUMMARY+". Today will be "+TEMP_FEELING+" with a high of "+str(HIGH_TEMP)+" and a low of "+str(LOW_TEMP)+". "+RAIN_WARNING
weather


# In[14]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y")


# In[15]:


date_string


# In[16]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox32923414644541fca4e0f5aae3e2f4e3.mailgun.org/messages",
        auth=("api", "XXXXXX"),
        data={"from": "Excited User <mailgun@sandbox32923414644541fca4e0f5aae3e2f4e3.mailgun.org>",
              "to": ["kazuhiro.kida@nex.nikkei.com"],
              "subject": "8AM Weather forecast: "+date_string,
              "text": weather}) 
response.text

