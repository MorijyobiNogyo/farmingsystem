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

	@abc.absabstructmethod
	def powerOn():
		"""機器をオンにするメソッド。"""
		pass

	@abc.absabstructmethod
	def PowerOff():
		"""機器をオフにするメソッド。"""
		pass
		