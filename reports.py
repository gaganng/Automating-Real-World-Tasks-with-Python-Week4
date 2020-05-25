#By Gagan Gundala
#Code Meant for Learning Purpose, not using for Coursera Submission.
#This code is highly in-efficient and not written with correct programming practices
#But it works!!!!

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

#Generates PDF report with whatever name and location given in filename
def generate_report(filename, title, additional_info):
    styles=getSampleStyleSheet()
    report=SimpleDocTemplate(filename)
    report_title=Paragraph(title, styles["h1"])
    report_info=Paragraph(additional_info, styles["BodyText"])
    empty_line=Spacer(1,20)
    report.build([report_title,empty_line,report_info])
