import qrcode 
import os
import random
from PIL import Image, ImageDraw
from flask_mail import Message
import email.message
from email.message import EmailMessage
from controllers import mail
from controllers import app

def send_qr_code(reciever_email, name):
    data = random.randint(100000,999999)
    img = qrcode.make(data)
    img.save("controllers/qr.png")
    msg = Message('Scan the QR Code', sender='testemailnyp@gmail.com', recipients=[reciever_email])
    msg.body = f'Customer Name:{name}\nCustomer Email: {reciever_email}\nScan the QR code below:\n'
    with app.open_resource("qr.png") as fp:
        msg.attach("qr.png", "qr/png", fp.read())
    mail.send(msg)
    os.remove("controllers/qr.png")
    return data


