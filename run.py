#By Gagan Gundala
#Meant for Learning Purpose.I do not recommend using it for Coursera Submission.
#This code is in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3
import json
import os
import requests
import re

#This function uploads fruit name, fruit weight(int) & fruit description one by one
def uplo_details():
    url='http://[linux-instance-ip-address]/fruits/'
    files_names=os.listdir('supplier-data/descriptions')
    image_names=os.listdir('supplier-data/images')
    fruit=list()
    tmp_dict=dict()
    new_image_names=list()

    #Creates new list with names of JPG format images only
    for j in image_names:                  #Ignores other files like README & LICENSE
        if not j.endswith('.tiff') and j!='README' and j!='LICENSE':
            new_image_names.append(j)

    #Creating a list of dictionaries called fruit. Each dictionary has 4 keys - name,weight,description & image name
    for file_name,image_name in zip(files_names,new_image_names):
        with open('supplier-data/descriptions/'+file_name) as f:
            file_text=f.readlines()
            tmp_dict['name']=file_text[0].strip()
            int_weight=int(re.sub(' lbs','',file_text[1].strip()))
            tmp_dict['weight']=int_weight
            tmp_dict['description']=file_text[2].strip()
            tmp_dict['image_name']=image_name
            fruit.append(tmp_dict.copy())

    #Sending data to API
    for i in fruit:
        resp=requests.post(url,data=i)

uplo_details()
