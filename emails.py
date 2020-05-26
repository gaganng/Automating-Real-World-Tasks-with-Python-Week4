#By Gagan Gundala
#Meant for Learning Purpose.I do not recommend using it for Coursera Submission.
#This code is in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib


#Generates Email Message
def generate_email(sender, recipient, subject, body, attachment_path=False):
    message=email.message.EmailMessage()
    message["From"]=sender
    message["To"]=recipient
    message["Subject"]=subject
    message.set_content(body)

    #Checks if attachment is to be sent with email message
    if attachment_path:
        attachment_filename=os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype=mime_type.split('/',1)
        with open(attachment_path,'rb') as ap:
            message.add_attachment(ap.read(),
                              maintype=mime_type,
                              subtype=mime_subtype,
                              filename=attachment_filename)
    return message

#Sends message generated in generate_email() function
def send_email(message):
    mail_server=smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
