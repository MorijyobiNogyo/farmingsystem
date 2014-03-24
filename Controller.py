#エンコードの指定
# -*- coding: utf-8 -*-

#モジュールのインポート
import abc
#Raspberry Piで使うときは解除する
#import RPi.GPIO as GPIO


#以下コード

class Controller(object, metaclass=abc.ABCMeta):


	"""コントローラの基底クラス。"""
	def __init__(self):
		pass

	@abc.abstractmethod
	def powerOn():
		"""機器をオンにするメソッド。"""
		pass

	@abc.abstractmethod
	def PowerOff():
		"""機器をオフにするメソッド。"""
		pass

class WateringController(Controller):
	"""ポンプを制御するクラス。"""
	def __init__(self):
		pass
		
	def powerOn(self):
		"""ポンプをオンにするメソッド"""
		pass

	def PowerOff(self):
		"""ポンプをオフにするメソッド"""
		pass

class LightingController(Controller):
	"""明かりを制御するクラス"""
	def __init__(self):
		pass

	def powerOn(self):
		"""明かりをつけるメソッド"""
		pass

	def PowerOff(self):
		"""明かりを消すメソッド"""
		pass