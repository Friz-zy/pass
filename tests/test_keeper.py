#!/usr/bin/env python2

import os,sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'maxi'))
from keepass import kpdb
from keeper import Keeper

test = kpdb.Database()

k = Keeper()
#print str(k.db)
k.load("./tests/test.kdb", "123")
#print str(k.db)
#print k.urls

k.db.add_entry("Internet","test","test","test","test","test",imageid=0,append=True)

k.db.add_entry("Internet","test1","test1","test1","test1","test1",imageid=0,append=True)

k.db.remove_entry("test1","test1")

#print str(k.db)
#print k.urls

k.save("./tests/test.kdb", "123")
print str(k.db)
k.load("./tests/test.kdb", "123")
print str(k.db)
#print k.urls

k.db.remove_entry("test","test")
k.save("./tests/test.kdb", "123")