# msg = Message(email_data['subject'],
#                   sender=app.config['MAIL_DEFAULT_SENDER'],
#                   recipients=[email_data['to']])

class Message:

    def __init__(self, subject='', body='', sender=None,recipients=[]):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.recipients = recipients
    
    def send(self):
        for recipient in self.recipients:
            message = f'Sender: {self.sender}\nRecipient: {recipient}\n'
            message += f'Subject: {self.subject}\nBody: {self.body}\n'
            print(message)