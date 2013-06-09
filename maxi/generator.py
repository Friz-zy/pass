#!/usr/bin/env python2
# coding=utf-8 

from time import clock
from itertools import cycle, izip
import sys
import random
import time
import hashlib
import os.path

class Generator():
	def __init__(self, parent):
		pass
      
      
	def set_salt(self, file):
		# check the unique salt
		salt = "##"
		with open(file, "r") as f:
			salt = f.readlines()
		# if salt isn't unique: add some unique string to it
		if "#" in salt[-1][1]:
			try:
				os.popen("(dmesg;env;head -c16 /dev/random)|sha512sum >> " + file)
				with open(file, "r") as f:
					salt = f.readlines()
				salt[-1]="#" + salt[-1]
				with open(file, "w") as f:
					f.writelines(salt)
				os.popen("chmod 400 " + file) # only your user can read this file
			except IOError, OSError:
				# it is works in all OS, but clock() is most efficient in Windows
				with open(file, "a") as f:
					f.writeline("#" + hashlib.sha512(clock()).hexdigest())
		with open(file, "r") as f:
			self.salt = f.read()

	def generate_simple(self, nikname = "", url = "", password = "", lenght = 32):
		lenght = int(lenght)
		if lenght > 512:
			lenght = 512
		nick = nikname + " : " + url
		firstXor = self.xor(self.salt, nick)
		firstSha = hashlib.sha512(firstXor).hexdigest()
		password = hashlib.sha512(self.xor(firstSha, str(password))).hexdigest()[:lenght]
		return password

	# XOR function, thk The Internet
	def xor(self, ss, key):
		key = cycle(key)
		return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))