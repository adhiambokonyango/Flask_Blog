from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'corona' or 'Hi' in incoming_msg:
        msg.body("Welcome to KENYA: COVID-19rerere")
        responded = True
    if not responded:
        msg.body('What would u like to know about the current outbreak?')
    return str(resp)
