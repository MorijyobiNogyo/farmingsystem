import abc

class Config(object, __metaclass__ = abc.ABCMeta):
	"""設定の読込み"""
	@abc.abstructmethod
	def load(Dictionary):
		pass

	"""設定の保存"""
	@abc.abstructmethod
	def save(Dictionary):
		pass