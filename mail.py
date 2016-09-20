# A function that sends the email of the result to hadas.c@velismedia.com.
import smtplib
def sendemail(perecent):
    from_addr = 'stasinterview@gmail.com'
    login = 'stasinterview'
    password = 'velismedia'
    smtpserver = 'smtp.gmail.com:587'
    to_addr_list = ['webnetinternet@gmail.com']
    cc_addr_list = ''
    subject = 'Velis Media assignment result'
    message = 'The error percentage of the classifier is {0}'.format(perecent)
    
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    print("Email sent")








