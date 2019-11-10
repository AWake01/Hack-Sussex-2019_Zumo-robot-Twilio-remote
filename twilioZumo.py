from flask import Flask, request, redirect
import twilio
from gpiozero import Robot
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
from time import sleep

#Motor setup
speed = 0.5

robot = Robot(left=(26,19),right=(20,16))

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])    #POST request to web hook (Ngrok tunnel)
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    
    # Get text message
    body = request.values.get('Body', None)
    
    # Get response
    resp = MessagingResponse()

    # Add a message
    if body == "f" or body == "1":  #Forward
       resp.message("Forwards!")
       robot.forward(speed)
       sleep(2)
       robot.stop()
    elif body == "b" or body == "2":    #Back
       resp.message("Backwards")
       robot.backward(speed)
       sleep(2)
       robot.stop()
    elif body == "l" or body == "3":    #Left
       resp.message("Left")
       robot.left(speed*2)
       sleep(1.5)
       robot.stop()
    elif body == "r" or body == "4":    #Right
       resp.message("Right")
       robot.right(speed*2)
       sleep(1.5)
       robot.stop()
    elif body == "dance":   #Dance
       resp.message("Party on!")
       robot.right(speed*2)
       sleep(2)
       robot.left(speed*2)
       sleep(2)
       robot.forward(speed)
       sleep(2)
       robot.backward(speed)
       sleep(2)
       robot.stop()
    
    else:   #Error
       resp.message("ERROR: " + str(body))
       robot.stop()

    return str(resp)

if __name__ == "__main__":  #Main program
    app.run(debug=True)
    
