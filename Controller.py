#エンコードの指定
# -*- coding: utf-8 -*-

#モジュールのインポート
import abc


#以下コード

class Controller(object, metaclass=abc.ABCMeta):
	"""その他のコントローラの基底クラス。"""
	def __init__(self, arg):
		super(Controller, self).__init__()
		self.arg = arg

	@abc.abstructmethod
	def powerOn():
		"""機器をオンにするメソッド。"""
		pass

	@abc.abstructmethod
	def PowerOff():
		"""機器をオフにするメソッド。"""
		pass
		