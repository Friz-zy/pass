#!/usr/bin/env python2

import os,sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'maxi'))

from keeper import Keeper

k = Keeper()
#print str(k.db)
k.load("./tests/test.kdb", "123")
print str(k.db)
print k.urls