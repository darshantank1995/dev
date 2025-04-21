import smtplib

def send_email():
    try:
        smtp_server = 'sandbox.smtp.mailtrap.io'
        port = 587
        username = '89ae1e8b2fcde4'
        password = 'b63b7d96625b65'

        from_email = 'darshantank2012@gmail.com'
        to_email = 'darshantank2012@gmail.com'

        subject = "Test Email from Mailtrap"
        body = "This is a test email using Mailtrap SMTP."
        message = f"Subject: {subject}\n\n{body}"

        # Connect
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_email, message)
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    send_email()
