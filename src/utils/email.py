import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_email(sender_email, receiver_email, password, transaction_id):
    subject = "Your Transaction ID"
    message_text = f"Your transaction ID is {transaction_id}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(message_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return True, "Email sent successfully"
    except Exception as e:
        return False, f"Failed to send email: {e}"