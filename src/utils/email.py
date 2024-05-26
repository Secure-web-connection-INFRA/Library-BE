from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from src.config import EmailConfig
from src.utils.customError import CustomException

class Email:
    def __init__(self, app) -> None:
        Email.mail = Mail(app)

    @classmethod
    def sendEmail(cls, template, email, **kwargs):  # Use **kwargs to accept additional keyword arguments
        try:
	        # Render the template with additional keyword arguments
            reset_email = render_template_string(template, **kwargs)
            # Send the email
            msg = Message(subject="Password Reset", sender="aswinrockz10@gmail.com", recipients=[email], html=reset_email)
            cls.mail.send(msg)
        except Exception as e:
            print(e)
            raise CustomException("Unable to send email")
