import smtplib
#specific smtp domain name and integer port 
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com',587)
smtpObj.ehlo()

my_email = #your email
password = #the password to your email

emails = [
    #email addresses you want to send the mail to
]

smtpObj.starttls()
#logs in 
smtpObj.login(my_email, password)
i = 0
subject = 'Subject: Subject.\n\nBody'
while i < len(emails):
    #loops through the emails list to email the subject and message to each person
    smtpObj.sendmail(my_email, emails[i],subject)
    i+=1


smtpObj.quit()
