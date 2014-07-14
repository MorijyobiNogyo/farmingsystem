#!/usr/bin/env python
#coding:utf-8

import spidev

class LightSensor()
	def get()

		__CE=0 #CE0端子のこと

		__electric_voltage = 3.3 #電源電圧
		__resistor = 1000 #NLJに接続した抵抗の値　1kΩくらい？

		spi = spidev.SpiDev()
		spi.open(0,CE)

		retspi = spi.xfer2([0x68, 0x00]) #CH0を使用、MSPから出力
		value = (retspi[0]*256+retspi[1]) & 0x3ff

		v_lux = value * electric_voltage / 1024
		lux = 2 * (v_lux / resistor) * 1000000
		return lux