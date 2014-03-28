import abc
import Parametic

class Writable(Parametic, __metaclass__ = abc.ABCMeta):
	def __init__(self, arg):
		super(Writable, self).__init__()
		self.arg = arg

	@abc.abstructmethod
	def write(Dictionary):
		pass