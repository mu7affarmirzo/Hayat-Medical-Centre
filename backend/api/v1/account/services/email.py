from email.message import EmailMessage
import ssl
import smtplib
from hayat_med_center.settings import EMAIL_HOST_PASSWORD


def send_email(receiver, code):
    sender = "nazarmamatovnurmuhammad7@gmail.com"
    #     # your password = "your password"
    password = EMAIL_HOST_PASSWORD

    subject = "Hayat Medical Center"

    body = f"{code}"

    message = EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['subject'] = subject
    message.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message.as_string())