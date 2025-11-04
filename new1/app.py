from flask import Flask, render_template_string, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Your email setup
EMAIL_ADDRESS = "ayushhh.2010@gmail.com"
EMAIL_PASSWORD = "glwp phpz dfcb gvgi"
TARGET_EMAIL = "ayushhh.2010@gmail.com"  # where you’ll receive the message

# Simple HTML template with buttons
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Quick Message</title>
    <style>
        body { font-family: Arial; background: #f4f4f4; text-align: center; padding-top: 50px; }
        .box {
            display: inline-block;
            background: white;
            border: 2px solid #ccc;
            border-radius: 10px;
            padding: 20px 40px;
            margin: 15px;
            cursor: pointer;
            transition: 0.3s;
            font-size: 20px;
            font-weight: bold;
        }
        .box:hover { background: #0078ff; color: white; }
    </style>
</head>
<body>
    <h2>Send a Quick Message 💌</h2>
    <div>
        <a class="box" href="/send/HII">HII</a>
        <a class="box" href="/send/IMS">I MISS YOU</a>
        <a class="box" href="/send/ILY">I LOVE YOU</a>
        <a class="box" href="/send/OK">OK</a>
    </div>
</body>
</html>
"""

def send_email(message):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TARGET_EMAIL
    msg['Subject'] = "Message from your friend 💬"
    msg.attach(MIMEText(message, 'plain'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/send/<message>')
def send(message):
    send_email(message)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
