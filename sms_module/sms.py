from twilio.rest import Client

#replace with personal token and ID
account_sid = '' 
auth_token = ''
client = Client(account_sid, auth_token)

#send a SMS message with given parameter and data
def sendSMS(type, data):
  if 10 <= data <= 50:
       message_body = "The temperature measured by RPi is {:.1f}°C. Pet likes the temperature.".format(data)
  else:
       message_body = "The temperature measured by RPi is {:.1f}°C. Pet hates the temperature.".format(data)
  message = client.messages.create(
   from_='+12513334882',
   body=message_body,
   to='+' #replace with registered phone number.
  )
  #testing for message sent
  print("Message successfully sent!")
