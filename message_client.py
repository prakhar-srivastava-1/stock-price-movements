from secrets import TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE
from twilio.rest import Client


class MessageClient:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.phone = TWILIO_PHONE
        self.auth_token = TWILIO_AUTH_TOKEN
        self.my_phone = MY_PHONE
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_alert(self, text_body):
        message = self.client.messages.create(
            body=text_body,
            from_=self.phone,
            to=self.my_phone
        )
        print(message.status)
