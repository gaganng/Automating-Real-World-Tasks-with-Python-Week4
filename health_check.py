#By Gagan Gundala
#Meant for Learning Purpose.I do not recommend using it for Coursera Submission.
#This code is in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

#Returns CPU usage in percentage
def check_cpu():
    cpu_usage=psutil.cpu_percent()
    return cpu_usage

#Returns IP address of localhost
def check_network():
    ip_addr=socket.gethostbyname('localhost')
    return ip_addr

#Returns available disk space percentage
def check_disk():
    tot,used,fre=shutil.disk_usage('/')
    available_space=fre/tot*100
    return available_space

#Returns available Memory/RAM in MB
def check_memory():
    mem=psutil.virtual_memory()
    return mem.available/1048576 #Exact conversion of Bytes to Mega Bytes

#Checking for abnormal conditions, if detected, flag is set to 1
flag=0
if check_cpu()>80:
    flag=1
    subject='Error - CPU usage is over 80%'
if check_network()!='127.0.0.1':
    flag=1
    subject='Error - localhost cannot be resolved to 127.0.0.1'
if check_disk()<20:
    flag=1
    subject='Error - Available disk space is less than 20%'
if check_memory()<500:
    flag=1
    subject='Error - Available memory is less than 500MB'

#Sends email if flag is 1
if flag==1:
    sender='automation@example.com'
    recipient='<username>@example.com'
    body='Please check your system and resolve the issue as soon as possible.'
    message=emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
