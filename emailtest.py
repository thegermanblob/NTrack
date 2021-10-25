import smtplib
gmail_user = "Ntrack@mail.com"
gmail_app_password = 
sent_from = gmail_user
sent_to = ['2594@holbertonschool.com']
sent_subject = 'Test'
sent_body = 'This is a test'
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
try:
        server = smtplib.SMTP_SSL('smtp.mail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text.encode("utf-8"))
        server.close()
        print(email_text)
        print('Email sent!')
except Exception as exception:
        print("Error: %s!\n\n" % exception)