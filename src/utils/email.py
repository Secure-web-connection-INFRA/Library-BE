from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from src.utils.constants import ConfigEnum
from src.utils.customError import CustomException


class Email:
    
    def config(self,app) -> Flask:
        # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        # app.config['MAIL_PORT'] = 587
        # app.config['MAIL_USE_TLS'] = True
        # # app.config['MAIL_USE_SSL'] = True
        # app.config['MAIL_USERNAME'] = ConfigEnum.EMAIL
        # app.config['MAIL_PASSWORD'] = ConfigEnum.PASSWORD
        # # Configure Flask-Mail
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USERNAME'] = 'kumarsaswin10@gmail.com'
        app.config['MAIL_PASSWORD'] = 'jxjvoxibblsdayjg'
        self.mail = Mail(app)
        return app

    def sendEmail(self, template, email, reset_url):
        try:
            reset_email = render_template_string(template, reset_url=reset_url)
            # Send the email
            msg = Message(subject="Password Reset",sender="aswinrockz10@gmail.com", recipients=[email], html=reset_email)
            self.mail.send(msg)
        except Exception as e:
            print(e)
            raise CustomException("Unable to send email")

email = Email()