import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "qhq5zcku2dbtzv5c@ethereal.email"
    login = "qhq5zcku2dbtzv5c@ethereal.email"
    password = "EJat6tXfmXX2FhYWDV"

    msg = MIMEMultipart()
    msg["from"] = "trip_confirmer@email.com"
    msg["to"] = ', '.join(to_addrs)
    msg["Subject"] = "Trip Confirmation"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()