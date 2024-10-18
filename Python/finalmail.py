import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
gmail_user = 'your_emai@gmail.com'
gmail_pwd = 'your_app_password'  # Use app password if 2FA is enabled

to = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent from Python!'

# Create the email
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Use TLS
        server.login(gmail_user, gmail_pwd)  # Login
        server.send_message(msg)  # Send email
        print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Failed to login. Check your username/password.")
except Exception as e:
    print(f"An error occurred: {e}")
