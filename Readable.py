import abc
import Parametic

class Readable(Parametic, __metaclass__ = abc.ABCMeta):
	def __init__(self, arg):
		super(Readable, self).__init__()
		self.arg = arg

	@abc.abstructmethod
	def read():
		pass