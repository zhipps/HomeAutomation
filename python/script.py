import webiopi
import datetime
#from nrf24 import NRF24
import time

GPIO = webiopi.GPIO


# setup function is automatically called at WebIOPi startup
def setup():
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
	

	
	

		
    return True
# destroy function is called at WebIOPi shutdown
# def destroy():

#def dataRX(RXbuf):
#	radio.startListening()
#	recv_buffer = []
#	radio.read(recv_buffer)
#	return recv_buffer
	
#def dataTX(TXbuf):
#	radio.stopListening()
#	radio.write(TXbuf)
#	return True 
