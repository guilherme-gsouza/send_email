### importing packages

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
    
### function to send email

def send_mail(subject, to, msg):

    Aux_Email = MIMEMultipart()

    Aux_Email['From'] = #myemail  

    Aux_Email['To'] = to #if you are going to send the e-mail for multiple recipients you must use ; to separate the adresses 
    
    Aux_Email['Subject'] = subject
    
    # Create the body of the message (a plain-text and an HTML version).

    message = msg   
    
    # Record the MIME types of both parts - text/plain and text/html.

    Aux_Email.attach(MIMEText(message, 'html'))   
    
    # Open the file that you want to attach

    attachment = open('/example/example/example.xlsx', 'rb')   

    file_name = os.path.basename('/example/example/example.xlsx')   

    part = MIMEBase('application','octet-stream')   

    part.set_payload(attachment.read())   
    
    # Attach the file to the e-mail

    part.add_header('Content-Disposition','attachment',filename=file_name)   

    encoders.encode_base64(part)  
    
    # Attach parts into message container.

    # According to RFC 2046, the last part of a multipart message, in this case

    # the HTML message, is best and preferred.

    Aux_Email.attach(part)
    
    # Send the message via local SMTP server.
    
    smtpserver = smtplib.SMTP('SMTP_SERVER')   
    
    # sendmail function takes 3 arguments: sender's address, recipient's address

    # and message to send - here it is sent as one string.

    smtpserver.sendmail(Aux_Email['From'], Aux_Email['To'].split(";"), Aux_Email.as_string())   

    smtpserver.quit()
