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
    # csv file should have, Mandotory : dpNo, partnerId, dpMailId 
    #                       Optional  : umMailId
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    with open('dp_qr_codes_Sept_batch1.csv', mode ='r') as file:
    #with open('test_qr_sample_data.csv', mode ='r') as file:
            # reading the CSV file
            csvFile = csv.DictReader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                            #print(lines)
                            if(lines['partnerId'] and "-" not in lines['partnerId']): 
                                print(lines['partnerId'] + " === " )
                                qr_content = "https://pro.turtlemint.com/insurance/group-products?partnerId=" + lines['partnerId']
                                img = qrcode.make(qr_content)
                                type(img)  # qrcode.image.pil.PilImage
                                base_path = "dp_qr_codes_Sept_batch1/"
                                qr_filename = base_path + lines['dpNo'].replace(" ","") + "-QRCode.png"
                                img.save(qr_filename)
                                print("QR Code generated for : " + lines['dpNo'] + "_" )
                            #else: 
                            #    print(lines['partnerId'] + " === " + lines['name'])
                                
                                #if(lines['dpMailId'] and "@" in lines['dpMailId']):
                                #    print("Sending QR Code to : " + lines['dpMailId'] )
                                    #send_mail(lines['dpMailId'],lines['umMailId'],qr_filename,qr_mail_subject,qr_mail_body)
                                #else:
                                #    print("Invalid mailid : " + lines['dpMailId'] + " for " + lines['dpNo']) 


def send_mail(toaddr,ccaddr,filename,subject,body):
    #fromaddr = "no-reply@turtlefin.com"
    #toaddr = "0"
    #ccaddr = "chetan.r@turtlemint.com"
    all_recipient = [toaddr,ccaddr] 

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the receivers email address
    msg['Cc'] = ccaddr
    # storing the subject
    #msg['Subject'] = "Test Mail with attachment & CC"
    # string to store the body of the mail
    #body = "Body_of_the_mail"
    msg['Subject'] = subject

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    #filename = "turtlefin-logo.png"
    #base_path = "/Users/chetanr/Desktop/qr-generator/"
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    #s=smtp_login(smtp_user,smtp_pass)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    print("Sending mail to "+ toaddr)
    # sending the mail
    smtp_session_custom = smtp_login(smtp_user,smtp_pass)
    smtp_session_custom.sendmail(fromaddr, all_recipient, text)
    smtp_session_custom.quit()
    #if test_conn_open(smtp_session_custom):
    #    smtp_session_custom.sendmail(fromaddr, all_recipient, text)
    #else:
    #    print("SMTP connection reset")
    #    smtp_session_custom = smtp_login(smtp_user,smtp_pass)
    #    smtp_session_custom.sendmail(fromaddr, all_recipient, text) 

    #s.sendmail(fromaddr, ccaddr, text)
    # terminating the session
    #smtp_session_custom.quit()


def smtp_login(smtp_user,smtp_pass):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(smtp_user,smtp_pass)
    return s

def test_conn_open(smtp_session_custom):
    try:
        status = smtp_session_custom.noop()[0]
    except:  # smtplib.SMTPServerDisconnected
        status = -1
    return True if status == 250 else False

#~~~ Setting mail subject & body ~~~~~
fromaddr = "no-reply@turtlefin.com"
smtp_user = fromaddr
smtp_pass = "25@Feb2021"

qr_mail_subject = "Your Personalised QR code"

qr_mail_body = """
                Dear Team,

                Happy to launch a new technology of QR code with which you will be able to easily sell personal accident product.
                Just scan the code with camera in your mobile and you'll be able to open a open mintpro wherein you can punch the policy.
                A customised QR code for you is attached in the mail. Please download and starts using.
                Looking forward to many personal accident policies through you and your QR code.                              

                Happy selling!                               

                *The above is strictly for Internal circulation only. Eligible for internal sales persons. For more details and T&C contact your manager.
                                
                We at TurtlemintPro are committed to providing the best services to you. If you are not interested to receive further communication, please click here to unsubscribe. 
                We do not endorse any particular company and/or product or plan or brand or services of any such corporate entity/company.

                ©️ 2022 TurtlemintPro. All Rights Reserved. Privacy Policy and Terms"""


#~~~~ Invoke QR code generation ~~~~
#smtp_session_custom = smtp_login(smtp_user,smtp_pass)

generate_QR()

#smtp_session_custom.quit()
#~~~~ END ~~~~~~~