from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from src.config import EmailConfig
from src.utils.customError import CustomException

class Email:

    def __init__(self,app) -> None:
        Email.mail = Mail(app)
    
    # def config(self, app:Flask) -> Flask:
    #     app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    #     app.config['MAIL_PORT'] = 587
    #     app.config['MAIL_USE_TLS'] = True
    #     app.config['MAIL_USERNAME'] = EmailConfig.MAIL_USERNAME
    #     app.config['MAIL_PASSWORD'] = ConfigEnum.PASSWORD.value
    #     self.mail = Mail(app)
    #     return app
    @classmethod
    def sendEmail(cls, template, email, reset_url):
        try:
            reset_email = render_template_string(template, reset_url=reset_url)
            # Send the email
            msg = Message(subject="Password Reset",sender="aswinrockz10@gmail.com", recipients=[email], html=reset_email)
            cls.mail.send(msg)
        except Exception as e:
            print(e)
            raise CustomException("Unable to send email")

# email = Email()