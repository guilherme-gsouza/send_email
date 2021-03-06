### importing packages

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
    
### function to send email

def send_mail(mesage, subject, to):

    msg = MIMEMultipart('alternative')

    msg['Subject'] = subject
    
    msg['From'] = #myemail

    msg['To'] = to #if you are going to send the e-mail for multiple recipients you must use ; to separate the adresses 

    # Create the body of the message (a plain-text and an HTML version).

    html = mesage

    # Record the MIME types of both parts - text/plain and text/html.

    part1 = MIMEText(html, 'html')

    # Attach parts into message container.

    # According to RFC 2046, the last part of a multipart message, in this case

    # the HTML message, is best and preferred.

    msg.attach(part1)

    # Send the message via local SMTP server.

    s = smtplib.SMTP('SMTP_SERVER')

    # sendmail function takes 3 arguments: sender's address, recipient's address

    # and message to send - here it is sent as one string.

    s.sendmail(msg['From'], msg['To'].split(";"), msg.as_string())

    s.quit()
