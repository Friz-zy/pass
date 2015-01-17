#!/usr/bin/env python
# http://python.su/forum/topic/8511/

import os

def getFiles(directory):
	if not os.path.exists(directory):
		return False
	Files = []
	for root, dirs, files in os.walk(directory):
		for f in files:
			Files.append(os.path.join(root,f))
	return Files



