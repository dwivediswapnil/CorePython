import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from']='Superman'
email['to']='swapnildwivedi26@gmail.com'
email['subject'] = 'You are the best.'
email.set_content('You are much more than you think!')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo() #part of protocol -smtp
    smtp.starttls() #encryption mechanism
    smtp.login('daemon123@gmail.com',"Pikachu123")
    smtp.send_message(email)
    print("all good boss!")

