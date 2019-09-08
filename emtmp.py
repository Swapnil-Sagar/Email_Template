import smtplib
import imghdr
import os
from email.message import EmailMessage

MY_EMAIL = os.environ.get('MY_EMAIL')


def send_email(to):
    message = EmailMessage()
    message['subject'] = "Swapnil Sagar CyberGeeks"
    message['from'] = MY_EMAIL
    message['to'] = "swapnil.swapnil.sagar946@gmail.com"
    message.set_content('Welcome to Cybergeek')
    html_message = open('template.html').read()
    message.add_alternative(html_message, subtype='html')

    # To Add any ATTACHMENT
    # with open('blurb_01.png','rb')as attach_file:
    #     image_name = attach_file.name
    #     image_type = imghdr.what(attach_file.name)
    #     image_data = attach_file.read()
    # message.add_attachment(image_data, maintype="image", subtype = image_type, filename =image_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465)as smtp:
        smtp.login(os.environ.get('MY_EMAIL'), os.environ.get('MY_PASS'))
        smtp.send_message(message)


send_email(MY_EMAIL)
