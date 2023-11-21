#Creating a email clint
import smtplib
from email.mime.text import MIMEText

body="This is a messege:How are you"

msg=MIMEText(body)
msg['From']='satishsubedi18@gmail.com'
msg['To']='swostikasubedi13@gmail.com'
me['subject']='Helllo mini sutkeri'

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('satishsubedi18','gmail@9861351199')
server.send_message(msg)

server.send(msg)

print('mail sent')
server.quit()
