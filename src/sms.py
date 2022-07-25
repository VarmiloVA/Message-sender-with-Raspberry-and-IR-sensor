from twilio.rest import Client 

def sms_send(text, phone_number):
    """La función que se encarga de enviar el sms a través de twilio"""
    #Código sacado de la propia documentación de twilio
    #Hay que dar de alta el número al que se quiera manda el SMS en: https://bit.ly/3k2GcLI.
 
    account_sid = '*****************************' 
    auth_token = '*****************************' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create(  
        messaging_service_sid='*************************', 
        body=text,      
        to=phone_number
    )