import time
from sinchsms import SinchSMS


number = '+5521981919603'
message = 'I love you!'
client = SinchSMS("a9350320-47a9-4de2-a6a6-783eac85ace9", "UV5SPK3aEUCSQcj0nopoPw==")
print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']
response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
time.sleep(1)
response = client.check_status(message_id)
print(response['status'])#  from twilio.rest import Client



### nao consegui fazer rodar. Tinham alguns custos embutidos