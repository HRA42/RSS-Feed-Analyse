import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, smtp_server, smtp_port, smtp_username=None, smtp_password=None):
    """
    Sends an email with the specified subject and message from the specified sender to the specified recipient(s).
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    # Create an SSL-encrypted SMTP connection
    smtp_conn = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp_conn.ehlo()

    if smtp_conn.has_extn('TLS'):
        smtp_conn.starttls()
        smtp_conn.ehlo()

    # If using authentication, login to the SMTP server
    if smtp_username is not None and smtp_password is not None:
        smtp_conn.login(smtp_username, smtp_password)

    # Send the email
    smtp_conn.sendmail(from_addr, to_addr, msg.as_string())

    # Close the SMTP connection
    smtp_conn.quit()
