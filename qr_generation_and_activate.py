# Import QR lib
import qrcode
import csv

# Import mail send lib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def generate_QR():
    # ~~~~~ opening the CSV file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # csv file should have, Mandotory : qrCodeUniqueId,externalId,redirectionLink 
    #                       Optional  : umMailId
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    with open('qr-activation-list.csv', mode ='r') as file:
    #with open('test_qr_sample_data.csv', mode ='r') as file:
            # reading the CSV file
            csvFile = csv.DictReader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                            #print(lines)
                            if(lines['qrCodeUniqueId']): 
                                #print( "Generating QRCode : " + lines['qrCodeUniqueId'])
                                #qr_content = "https://pro.skyfall.turtle-feature.com/qr-codes/activation?qrCodeUniqueId="+lines['qrCodeUniqueId']
                                qr_content = "https://pro.turtlemint.com/qr-codes/activation?qrCodeUniqueId="+lines['qrCodeUniqueId']
                                #https://app.turtlefin.com/qr-codes/activation?qrCodeUniqueId=123
                                img = qrcode.make(qr_content)
                                type(img)  # qrcode.image.pil.PilImage
                                base_path = "./"
                                qr_filename = base_path + lines['qrCodeUniqueId'] + ".png"
                                img.save(qr_filename)
                                #print("QR Code generated for : " + lines['qrCodeUniqueId'])
                                qr_link = "https://d15ymu0lcwxhb8.cloudfront.net/"+lines['qrCodeUniqueId']+".png"
                                #qr_link = "https://qrcode.mintpro.in/"+lines['qrCodeUniqueId']+".png"
                                
                                print(qr_link)

generate_QR()