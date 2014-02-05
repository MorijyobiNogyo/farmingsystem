# -*- coding: utf-8 -*-

class FarmingsystemMain(object):
	"""
	農業システムの中心になるクラスです。
	"""
	def __init__(self, arg):
		super(FarmingsystemMain, self).__init__()
		self.arg = arg
		
class TemperatureSensor(object):
	"""
	温度センサーに関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super(TemperatureSensor, self).__init__()
		self.arg = arg
		
class HumiditySensor(object):
	"""
	湿度センサーに関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super HumiditySensor, self).__init__()
		self.arg = arg
		
class OpticalSensor(object):
	"""
	光センサーに関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super(OpticalSensor, self).__init__()
		self.arg = arg
		
class CameraSensor(object):
	"""
	カメラに関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super(CameraSensor, self).__init__()
		self.arg = arg

class WaterPump(object):
	"""
	ポンプに関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super(WaterPunp, self).__init__()
		self.arg = arg
		
class Bulb(object):
	"""
	電球に関するクラスです。

	使用するGPIO:
	"""
	def __init__(self, arg):
		super(Bulb, self).__init__()
		self.arg = arg
		