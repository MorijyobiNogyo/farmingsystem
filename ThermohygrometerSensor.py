import dhtreader

class ThermohygrometerSensor()
	def get()
		dhtreader.init()
		
		dev_type = 11
		dhtpin = 4
		
		t, h = dhtreader.read(dev_type, dhtpin)
		
		return t, h