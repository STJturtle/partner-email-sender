import qrcode
import csv
from mail_send_2 import send_email
  
# opening the CSV file
with open('./partners.csv', mode ='r') as file:

        # reading the CSV file
        csvFile = csv.DictReader(file)

        # displaying the contents of the CSV file
        for lines in csvFile:
                        #print(lines)
                        print(lines['partnerId'] + " === " + lines['name'])
                        qr_content = "https://pro.turtlemint.com/insurance/group-products?partnerId=" + lines['partnerId']
                        img = qrcode.make(qr_content)
                        type(img)  # qrcode.image.pil.PilImage
                        img.save("./qrcodes/" + lines['dpNo'] + "_" + lines['name'] + "-QRCode.png")
                        print("QR Code generated for DP : " + lines['dpNo'] + "_" + lines['name'])
                        send_email()
print("Done..")

