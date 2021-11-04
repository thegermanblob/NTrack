import smtplib

import requests

id = "6170be1ace938dab7b685232"
ticket_id = "6170be1ace938dab7b685231"
url_client = "https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/client/" + id
url_ticket = "https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/ticket/" + ticket_id

client = requests.get(url=url_client).json()
ticket = requests.get(url=url_ticket).json()
print(client['client_email'])
client_name = client['client_name']
ticket_status = ticket['status']
ticket_description = ticket['description']

html_content = f"Dear, {client_name}!<br><br>Your ticket status has changed to:{ticket_status}. Please find the details below:<br><br>Ticket ID: {ticket_id} <br>Ticket Description: {ticket_description}<br>Ticket Status: {ticket_status}<br><br>Regards,<br>NTrack Team"

s = smtplib.SMTP('in-v3.mailjet.com', 587)

# Start TLS encryption
s.starttls()

# Login
s.login('NTrack', 'bc8f4a4e79f6739501b8e8f1d1305065')
url_client = "https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/client/" + id
url_ticket = "https://2ktpylu8p5.execute-api.us-east-2.amazonaws.com/dev/api/v1/ticket/" + ticket_id

sender = 'NTrack@mail.com'
receivers = str(client['client_email'])

message = """From: From NTrack <NTrack@mail.com>
To: {} <{}>
Subject: SMTP e-mail test

{}
""".format(client_name, receivers, html_content)

try:
    s.sendmail(sender, receivers, message)
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
