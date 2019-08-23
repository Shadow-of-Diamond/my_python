#! /usr/local/bin/python3
# -*- coding: UTF-8 -*-
from twilio.rest import Client

# put your own credentials here
accountSID = 'AC0a34654759cdfc833092d690fa7ba63d'
authToken = 'b1eee126e710f45274a6de02aaf93bfe'

#myNumber = '+86 19928326285'
myNumber = '+86 15915897669'

twilioNumber = '+1 716 221 8087'
#message = "This is a test message for twilio and python test."
message = "python脚本发送中文短信测试"
client = Client(accountSID, authToken)

client.messages.create(
    to=myNumber,
    from_=twilioNumber,
    body=message
    #media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg"
)
print ('短信发送成功')