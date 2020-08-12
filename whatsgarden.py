from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'water' in incoming_msg:
        # return a quote
        msg.body("Plant is being watered")
        responded = True
    if not responded:
        msg.body('Cannot operate the previous order')
    return str(resp)

if __name__ == '__main__':
    app.run()
