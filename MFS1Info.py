import abc

class MFS1Info(object, __metaclass__ = abc.ABCMeta):
	@abc.abstructmethod
	def name():
		pass

	@abc.abstructmethod
	def version():
		pass

	@abc.abstructmethod
	def gpio(string):
		pass