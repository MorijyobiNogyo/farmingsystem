import abc
import MFS1Info
import Readable

class Sensor(Readable, MFS1Info, __metaclass__ = abc.ABCMeta):