from datetime import date
import os
#By Gagan Gundala
#Meant for Learning Purpose, not using for Coursera Submission.
#This code is highly in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3
import reports
import emails


today=date.today() #Gets today's date

#Generates pdf's body text
def gen_para():
    files_names=os.listdir('supplier-data/descriptions')
    para=''
    for file_name in files_names:
        with open('supplier-data/descriptions/'+file_name) as f:
            file_text=f.readlines()
            para=para+'name: '+file_text[0].strip()+'<br/>'+'weight: '+file_text[1].strip()+$
    return para

if __name__ == "__main__":
    t_date=today.strftime("%B %d, %Y") #Returns today's date in 'Month_Name day, year' format
    attachment='/tmp/processed.pdf'
    title='Processed Update on '+t_date
    paragraph=gen_para()
    reports.generate_report(attachment, title, paragraph)
    sender='automation@example.com'
    recipient='[username]@example.com' #Username goes here
    subject='Upload Completed - Online Fruit Store'
    body='All fruits are uploaded to our website successfully. A detailed list is attached to the mail'
    attachment_path='/tmp/processed.pdf'
    msg=emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(msg)
