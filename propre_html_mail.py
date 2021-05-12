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

def add_file_html(file_name, file_path):
  html_data = f"""
  <div class="u-row-container" style="padding: 0px;background-color: #000000">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #000000;">
      <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #000000;"><![endif]-->
        
  <!--[if (mso)|(IE)]><td align="center" width="300" style="background-color: #000000;width: 300px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
  <div class="u-col u-col-50" style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
    <div style="background-color: #000000;width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
  <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
          
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="font-size: 14px; line-height: 140%; text-align: center; white-space: nowrap;
      width: 300px;
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;"><span style="color: #ecf0f1; font-size: 20px; line-height: 28px; font-family: 'Lato', sans-serif;">{file_name}</span></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
  <!--[if (mso)|(IE)]></td><![endif]-->
  <!--[if (mso)|(IE)]><td align="center" width="300" style="width: 300px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
  <div class="u-col u-col-50" style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
    <div style="width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
  <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
          
    <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
      <p style="font-size: 14px; line-height: 140%; text-align: center; white-space: nowrap;
      width: 300px;
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;"><span style="color: #ecf0f1; font-size: 20px; line-height: 28px; font-family: 'Lato', sans-serif;">{file_path}</span></p>
    </div>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
  <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
      </div>
    </div>
  </div>



  <div class="u-row-container" style="padding: 0px;background-color: #000000">
    <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #000000;">
      <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: #000000;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: #000000;"><![endif]-->
        
  <!--[if (mso)|(IE)]><td align="center" width="600" style="background-color: #000000;width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
  <div class="u-col u-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
    <div style="background-color: #000000;width: 100% !important;">
    <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
    
  <table style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
    <tbody>
      <tr>
        <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
          
    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="55%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
      <tbody>
        <tr style="vertical-align: top">
          <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
            <span>&#160;</span>
          </td>
        </tr>
      </tbody>
    </table>

        </td>
      </tr>
    </tbody>
  </table>

    <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
    </div>
  </div>
  <!--[if (mso)|(IE)]></td><![endif]-->
        <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
      </div>
    </div>
  </div>


  """
  return html_data

def make_csv(data):
    csv_file = 'Transaction ID,File Name,File Path\n'
    for file_name in data["Files Path"]:
        csv_file+= f'{data["Transaction"]["txid"]},{file_name},{data["Files Path"][file_name]}\n'
    return csv_file.encode()

def send_email(strFrom, strTo, PASSWORD, data):

    with open('index.html', 'r') as f:
        html_text = f.read()
    
    html_text = html_text.replace("TX_ID", data["Transaction"]["txid"])

    html_text = html_text.replace("_BLOCKCHAIN_LINK_", data["Transaction"]["blockchain"])

    plain_text = 'Dear User,\n\nPlease find your transaction details below. \n\n'
    plain_text += f'Transaction ID: {data["Transaction"]["txid"]}\n\n'

    path_html = ''

    for file_name in data["Files Path"]:
        path_html += add_file_html(file_name, data["Files Path"][file_name])
        plain_text += f'{file_name}: {data["Files Path"][file_name]}\n'
    
    html_text = html_text.replace("_ROW_DATA_", path_html)

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

    fp = open('images\logo.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<logo>')
    msgRoot.attach(msgImage)

    fp = open('images\github.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<github>')
    msgRoot.attach(msgImage)

    fp = open('images\email.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<email>')
    msgRoot.attach(msgImage)

    fp = open('images\linkedin.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<linkedin>')
    msgRoot.attach(msgImage)
 
    json_attachment = MIMEBase('application', 'octet-stream')
    json_attachment.set_payload(json.dumps(data, indent=4).encode())
    encoders.encode_base64(json_attachment)
    json_attachment.add_header('Content-Disposition', "attachment; filename= %s" % 'transaction_details.json')
    msgRoot.attach(json_attachment)

    csv_attachment = MIMEBase('application', 'octet-stream')
    csv_attachment.set_payload(make_csv(data))
    encoders.encode_base64(csv_attachment)
    csv_attachment.add_header('Content-Disposition', "attachment; filename= %s" % 'transaction_details.csv')
    msgRoot.attach(csv_attachment)

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
