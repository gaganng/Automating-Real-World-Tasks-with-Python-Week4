#By Gagan Gundala
#Meant for Learning Purpose, not using for Coursera Submission.
#This code is highly in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3
import requests
import os

#This function uploads images to API
def uplo_img():
    url='http://[linux-instance-ip-address]/upload/' #Linux instance ip address goes here
    img_names=os.listdir('supplier-data/images')
    for image_name in img_names:
        if image_name.endswith('.jpeg'):
            with open('supplier-data/images/'+image_name,'rb') as im:
                resp=requests.post(url,files={'file':im})

uplo_img()
