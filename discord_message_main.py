#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[2]:


def discord_message(channel_id):
    headers={
        'authorization':'MTA0MTI3MTA1MDIwMzMwODA1NQ.GqjmFD.zuEV8eJodVQFRnCPLj69O6x1STdjHjjC_M9gnQ'
    }
    response=requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers)
    jsson=json.loads(response.text)
    for value in jsson:
        print(value,"\n")


# In[3]:


discord_message('1116648086408802304')


# In[82]:




