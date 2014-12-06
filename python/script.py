import webiopi
import datetime
from nrf24 import NRF24
import time

GPIO = webiopi.GPIO
relay = 11

HOUR_ON = 17
HOUR_OFF = 23

# setup function is automatically called at WebIOPi startup
def setup():

    GPIO.setFunction(relay, GPIO.OUT)
   # pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]
   # radio = NRF24()
   # radio.begin(1, 0,"P8_23","P8_24")
   # radio.setRetries(15,15)
   # radio.setPayloadSize(8)
   # radio.setChannel(0x60)
   # radio.setDataRate(NRF24.BR_250KBPS)
   # radio.setPALevel(NRF24.PA_MAX)
   # radio.setAutoAck(1)
   # radio.openWritingPipe(pipes[0])
   # radio.openReadingPipe(1, pipes[1])
   # radio.printDetails()
    return True
# loop function is repeatedly called by WebIOPi 
def loop():
    	
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0)):
        if (GPIO.digitalRead(relay) == GPIO.HIGH):
            GPIO.digitalWrite(relay, GPIO.LOW)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0)):
        if (GPIO.digitalRead(relay) == GPIO.LOW):
            GPIO.digitalWrite(relay, GPIO.HIGH)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.HIGH)
    return True

#def dataRX(RXbuf):
#	radio.startListening()
#	recv_buffer = []
#	radio.read(recv_buffer)
#	return recv_buffer
	
#def dataTX(TXbuf):
#	radio.stopListening()
#	radio.write(TXbuf)
#	return True 
