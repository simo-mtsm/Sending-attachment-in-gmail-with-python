
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




msg = MIMEMultipart()                                                       #inistaliz the protocol MIME

msg['From'] = 'yourEmail@gmail.com'
msg['Subject'] = 'Demande de khedma!!!!'

FileList=open('Fileliste.txt', 'rb')

for eMail in FileList:
   msg['To']=eMail
   filename='yourCv.doc'
   attachment  =open(filename,'rb')                                         # Your Cv

   part = MIMEBase('application','octet-stream')                            # Content-types
   part.set_payload((attachment).read())                                    # Upload the CV
   encoders.encode_base64(part)                                             # encoding with base_64
   part.add_header('Content-Disposition',"attachment; filename= "+filename) #description the content

   msg.attach(part)
   text = msg.as_string()
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(msg['From'],'Password')
   server.sendmail(msg['From'],msg['To'],text)


server.quit()