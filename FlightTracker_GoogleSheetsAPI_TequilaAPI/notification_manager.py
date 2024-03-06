import smtplib
from email.mime.text import MIMEText

# Replace with your actual Gmail address and password
EMAIL = "Enter your email"
PASSWORD = "Enter your Password"

class NotificationManager:
    def __init__(self, email):
        self.email = email

    def send_email(self, city, price, lowest_price):
        message = MIMEText(f"Great deal found for {city}!\nCurrent price: {price}, lowest recorded price: {lowest_price}")
        message["Subject"] = "DEAL FOUND!"  # Set the subject line
        message["From"] = EMAIL
        message["To"] = EMAIL

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=message.as_string()
            )
