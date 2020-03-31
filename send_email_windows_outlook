## importing packages

import win32com.client as win32

## set the function to send email ... this function will use outlook and deffault account to send the email

def send_mail(to):
  
  outlook = win32.Dispatch('outlook.application')

  mail = outlook.CreateItem(0)

  mail.To = to #if you are going to send the e-mail for multiple recipients you must use ; to separate the adresses 

  mail.Subject = 'Message subject'

  mail.Body = 'Message body' #this field is optional, use this field if you want to send the message is not in HTML

  mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional, use this field if you want to send the message is in HTML

  mail.Send()
  
  
  
## set the function to send email ... this function will use outlook and you set the account that you want to send the email

def send_mail(to):
  
    o = win32com.client.Dispatch("Outlook.Application")

    oacctouse = None

    for oacc in o.Session.Accounts:

      if oacc.SmtpAddress == "SENDER_EMAIL":

        oacctouse = oacc

        break

    Msg = o.CreateItem(0)

    if oacctouse:

        Msg._oleobj_.Invoke(*(64209, 0, 8, 0, oacctouse))  # Msg.SendUsingAccount = oacctouse

    Msg.To= to #if you are going to send the e-mail for multiple recipients you must use ; to separate the adresses 

    Msg.Subject = 'Message subject'

    Msg.CC = #this field is optional, use this field if you want to send the e-mail with a adress in copy

    Msg.BCC = #this field is optional, use this field if you want to send the e-mail with a adress in hide copy

    Msg.Body = 'Message body' #this field is optional, use this field if you want to send the message is not in HTML

    Msg.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional, use this field if you want to send the message is in HTML

    Msg.Send()
