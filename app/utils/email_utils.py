from flask_mail import Mail, Message
from config import AUTH_EMAIL,SEND_EMAIL_TO
from threading import Thread

# Initialize Mail outside functions
mail = Mail()

def send_email(data):
    """
    Send an email.
    
    :param subject: Email subject
    :param sender: Sender email
    :param recipients: List of recipient emails
    :param body: Plain text body
    :param html: Optional HTML body
    """
    try:
        sender = AUTH_EMAIL
        recipients = [ SEND_EMAIL_TO ] 
        subject = "New client visit website!."
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = data
        mail.send(msg)
        print("Send done!.")
        return True
    except Exception as e:
        print(f"Error : {str(e)}")
        return False, str(e)
