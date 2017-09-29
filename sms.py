# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:24:01 2017

@author: Risa
"""
from twilio.rest import Client

account = "AC944e61af65b03b17801242f9b82b6f34"
token = "802fa929a1ae729f95b2622e6544f339"
client = Client(account, token)

message = client.messages.create(to="+19143090430",
                           from_="+12019879174",
                           body="THIS IS THE BODY YOU CAN MODIFY.")
print(message.sid)