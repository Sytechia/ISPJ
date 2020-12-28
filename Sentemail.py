import smtplib
from email.message import EmailMessage
from flask_mail import Message
from controllers import mail

def sendEmail(reciever_email, name, message, subject):
    msg = Message('Customer Enquiry', sender='testemailnyp@gmail.com', recipients=['testemailnyp@gmail.com'])
    msg.body = f'Customer Name:{name}\nCustomer Email: {reciever_email}\nCustomer Message:\n{message}'
    mail.send(msg)

def adminEmail(reciever_email):
    msg = Message('Failed attempts', sender='testemailnyp@gmail.com', recipients=['testemailnyp@gmail.com'])
    msg.body = f'Customer Email: {reciever_email} has failed to login after 5 attempts'
    mail.send(msg)



