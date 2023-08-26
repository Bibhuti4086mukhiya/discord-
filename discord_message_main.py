#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[2]:


def discord_message(channel_id):
    headers={
        'authorization':''
    }
    response=requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers)
    jsson=json.loads(response.text)
    # for value in jsson:
    #     print(value,"\n")
    return jsson


# In[3]:


discord_message('1116648086408802304')


# In[82]:




