import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

# Define email sender and receiver
email_sender = 'EMAIL@gmail.com'
email_password = 'PASSWORD16DIGITVERIFICATION'
# email_receiver = 'The email of the receiver'

# Set the subject and body of the email
subject = 'Try Send Email!'
body = """
Semangat sobat damen!<br>
Intinya Gitu<br>
:> hwhwhw
"""

# Reading the CSV file
csv_path = 'amultiple_emails.csv'
emails_df = pd.read_csv(csv_path)

# Looping through the CSV file and sending emails with attachments
# Looping through the CSV file and sending emails without attachments
for index, row in emails_df.iterrows():
    email_receiver = row['Receiver']

    # Define email parameters
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Make the message multipart
    em.add_alternative(body, subtype='html')

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
