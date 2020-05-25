#By Gagan Gundala
#Meant for Learning Purpose, not using for Coursera Submission.
#This code is highly in-efficient and not written with correct programming practices
#But it works!!!!
#!/usr/bin/env python3

from PIL import Image
import os

#Resizes images to 600x400 and converts them from .tiff to .jpeg
def update_images():
    img_names=os.listdir('supplier-data/images')
    for image_name in img_names:
        if image_name=='README' or image_name=='LICENSE': continue  #Ignore extra files called readme & license in the images directory
        im_obj=Image.open('supplier-data/images/'+image_name)
        im_obj=im_obj.resize((600,400))
        im_obj=im_obj.convert("RGB")
        image_name=image_name[:3]
        im_obj.save('supplier-data/images/'+image_name+'.jpeg')

update_images()
