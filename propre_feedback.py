from dotenv import load_dotenv
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
from threading import Thread
from os import environ

def send_email(strFrom, strTo, PASSWORD, data):

    plain_text = 'Respected Sir,\n\nA new feedback has been received on the wesbite. \n\n'
    for key in data:
        plain_text += f'{key}: {data[key]}\n\n'

    plain_text += '\nThank you.\n\nSincerely,\nPROPRE\n'

    msgRoot = MIMEMultipart('related')

    msgRoot['Subject'] = '[PROPRE] Feedback'
    msgRoot['From'] = "PROPRE <" + strFrom + ">"
    msgRoot['To'] = strTo

    msgRoot.preamble = '====================================================='

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(plain_text)
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(strFrom, PASSWORD)
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

def send_feedback(data):
        
    load_dotenv(dotenv_path='.env')

    EMAIL_ID = environ.get("EMAIL_ID")
    PASSWORD = environ.get("PASSWORD")

    email_thread = Thread(target=send_email, args=(EMAIL_ID, EMAIL_ID, PASSWORD, data))
    email_thread.start()
