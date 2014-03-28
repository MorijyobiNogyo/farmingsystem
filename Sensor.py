import abc
import MFS1Info
import Readable

class Sensor(Readable, MFS1Info, __metaclass__ = abc.ABCMeta):
	@abc.abstractmethod
	def get():
		pass

# 温度の値読込むクラス
class LightSensor(Sensor):
	def get():
		pass

# 湿度の値読込むクラス
class ThermohygrometerSensor(Sensor):
	def get():
		pass

# 画像読込むクラス
class ImageSensor(Sensor):
	def get():
		pass