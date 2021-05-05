from dotenv import load_dotenv
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from threading import Thread
from os import environ

def send_email(strFrom, strTo, PASSWORD, data):

    html_text = 'Dear User, <br> <br>Please find your transaction details below.<br><br>'
    html_text += f'<i>Transaction ID</i>: {data["Transaction ID"]}<br><br>'

    plain_text = 'Dear User,\n\nPlease find your transaction details below. \n\n'
    plain_text += f'Transaction ID: {data["Transaction ID"]}\n\n'

    for file_name in data["Files Path"]:
        html_text += f'<i>{file_name}</i>: {data["Files Path"][file_name]}<br>'
        plain_text += f'{file_name}: {data["Files Path"][file_name]}\n'
        
    html_text += '<br>Thank you for choosing us. <br><br>Sincerely,<br><b>PROPRE </b><br><br><img src="cid:image1"><br>'
    plain_text += '\nThank you for choosing us.\n\nSincerely,\nPROPRE\n'

    msgRoot = MIMEMultipart('related')

    msgRoot['Subject'] = '[PROPRE] Transaction Details'
    msgRoot['From'] = "PROPRE <" + strFrom + ">"
    msgRoot['To'] = strTo

    msgRoot.preamble = '====================================================='

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText(plain_text)
    msgAlternative.attach(msgText)
 
    msgText = MIMEText(html_text, 'html')
    msgAlternative.attach(msgText)

    fp = open('small_logo.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(strFrom, PASSWORD)
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()

def make_email(strTo, data):
        
    load_dotenv(dotenv_path='.env')

    EMAIL_ID = environ.get("EMAIL_ID")
    PASSWORD = environ.get("PASSWORD")

    email_thread = Thread(target=send_email, args=(EMAIL_ID, strTo, PASSWORD, data))
    email_thread.start()
