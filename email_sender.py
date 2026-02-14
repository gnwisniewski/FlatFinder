import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from listings import Listing, PriceUpdate
from config import SENDER, RECIPIENT, SMTP_SERVER, SMTP_PORT, SMTP_PASSWORD

def sendEmail(new_listings: list[Listing], price_updates: list[PriceUpdate]):
    subject = f"FlatFinder - New update"
    msg = MIMEMultipart("related")
    msg["From"] = SENDER
    msg["To"] = RECIPIENT
    msg["Subject"] = subject

    alt_part = MIMEMultipart("alternative")
    msg.attach(alt_part)

    text = "Your email client does not support HTML emails."
    alt_part.attach(MIMEText(text, "plain"))

    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif;">
        <h2>New updates</h2>
        <hr>
    """

    if new_listings:
        html += "<h3>New Listings</h3><ul style='list-style:none; padding:0;'>"
        for listing in new_listings:
            html += f"""
            <li style="margin-bottom:20px;">
                <h4>{listing.name}</h4>
                <img src="{listing.image_link}" style="width:300px;"><br>
                <strong>Price:</strong> {listing.price}<br>
                <a href="{listing.link}">View listing</a>
            </li>
            <hr>
            """
            html += "</ul>"

    if price_updates:
        html += "<h3>Price Updates</h3><ul style='list-style:none; padding:0;'>"
        for update in price_updates:
            html += f"""
            <li style="margin-bottom:20px;">
                <h4>{update.listing.name}</h4>
                <img src="{update.listing.image_link}" style="width:300px;"><br>
                <strong>Old price:</strong> {update.old_price}<br>
                <strong>New price:</strong> {update.listing.price}<br>
                <a href="{update.listing.link}">View listing</a>
            </li>
            <hr>
            """
            html += "</ul>"

    html += "</body></html>"

    alt_part.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER, SMTP_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully.")