#!/usr/bin/env python
# coding=utf-8 

import six
from time import clock
if six.PY3:
    from itertools import cycle
    izip = zip
else:
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
		if not self.check_salt(file):
			self.generate_salt(file)
		with open(file, "r") as f:
			self.salt = f.read()

	def check_salt(self, file):
		"default salt have ## in last string by default"
		salt = "##"
		with open(file, "r") as f:
			salt = f.readlines()
		if "#" in salt[-1][1] or "#" not in salt[-1][0]:
			return False
		return True

	def generate_salt(self, file):
		try:
			os.popen("(dmesg;env;head -c16 /dev/random)|sha512sum >> " + file)
			with open(file, "r") as f:
				salt = f.readlines()
			salt[-1]="#" + salt[-1]
			with open(file, "w") as f:
				f.writelines(salt)
			os.chmod(file, 256) # only your user can read this file
		except (IOError, OSError):
			# it is works in all OS, but clock() is most efficient in Windows
			with open(file, "a") as f:
				f.writeline("#" + hashlib.sha512(clock()).hexdigest())
			try:
				os.chmod(file, 256) # only your user can read this file
			except OSError:
				pass

	def generate_simple(self, nikname = "", url = "", password = "", lenght = 32):
		lenght = int(lenght)
		if lenght > 512:
			lenght = 512
		nick = nikname + " : " + url
		firstXor = self.xor(self.salt, nick)
		firstSha = hashlib.sha512(firstXor).hexdigest()
		password = hashlib.sha512(self.xor(firstSha, str(password))).hexdigest()[:lenght]
		return password

	def xor(self, ss, key):
		key = cycle(key)
		return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))
