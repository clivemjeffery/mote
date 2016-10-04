from mote import Mote
import time

mote = Mote()
mote.configure_channel(1, 16, False)

def moteshow(n):
	# show n lights on the strip
	mote.clear()
	if n < 0:
		raise IndexError()
	elif n > 16:
		raise IndexError()
	else:
		for pixel in range(n):
			mote.set_pixel(1, pixel, 255, 0, 0)
		mote.show()

moteshow(2)
time.sleep(2)
moteshow(4)
time.sleep(2)
moteshow(10)
time.sleep(2)
moteshow(16)
time.sleep(2)
moteshow(0)
