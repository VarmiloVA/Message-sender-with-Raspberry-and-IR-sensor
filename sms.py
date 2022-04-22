from typing import Text
from twilio.rest import Client 

def sms_send(text):
    """Sends the SMS"""
    #Hay que dar de alta el número en cuestion.
 
    account_sid = 'ACef0867a31b82b7fcc145855083dc6477' 
    auth_token = '5dd20f4c22df3e9d06154762faad39ef' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create(  
                              messaging_service_sid='MGbda50f472a898a67b63118b29fc05c45', 
                              body='Verificación para su cuenta de pornhub.com',      
                              to='+34698985297' 
                          ) 
 
    print(message.sid)
