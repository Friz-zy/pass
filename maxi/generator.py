#!/usr/bin/env python
# coding=utf-8
"""
Copyright (c) by Filipp Kucheryavy aka Frizzy <filipp.s.frizzy@gmail.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:

a. Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer. 

b. Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution. 

c. Neither the name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS 
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
