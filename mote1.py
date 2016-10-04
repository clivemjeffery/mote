from mote import Mote
import time

mote = Mote()
mote.configure_channel(1, 16, False)

while True:
	for pixel in range(16):
		mote.clear()
		mote.set_pixel(1, pixel, 0, 255, 0)
		mote.show()
		time.sleep(0.05)
	for pixel in range(15, -1, -1):
		mote.clear()
		mote.set_pixel(1, pixel, 0, 0, 255)
		mote.show()
		time.sleep(0.05)