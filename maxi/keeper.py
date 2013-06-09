#!/usr/bin/env python2
# coding=utf-8 
"""
self.entries = []


add_entry(self,path,title,username,password,url="",notes="",imageid=1,append=True):
new_entry = infoblock.EntryInfo()
            new_entry.uuid = self.gen_uuid()
            new_entry.groupid = group.groupid
            new_entry.imageid = imageid
            new_entry.title = title
            new_entry.url = url
            new_entry.username = username
            new_entry.password = password
            new_entry.notes = notes
            
use ony Internet group
"""
try:
	from keepass import kpdb
except: pass


class Keeper():
	def __init__(self, parent = None):
		try:
			self.db = kpdb.Database()
			self.isKdb = True
		except:
			self.db = None
			self.isKdb = False
		self.urls = {}
		
	def load(self, file, password = ""):
		if self.isKdb:
			self.db = kpdb.Database(str(file), str(password))
			for entry in self.db.entries:
				self.urls[entry.url] = {entry.username : [entry.password, entry.notes]}
		else:
			pass
	
	def sync_entries(self):
		if self.isKdb:
			urls = {}
			for entry in self.db.entries:
				urls[entry.url] = {entry.username : [entry.password, entry.notes]}
			# delete all entries than not in urls:pass
			for url in urls.keys():
				for name in urls[url].keys():
					try:
						if name not in self.urls[url].keys(): 
							self.db.remove_entry(name,url)
					except:
						self.db.remove_entry(name,url)
			# add all urls:pass that not in entries
			for url in self.urls.keys():
				for name in self.urls[url].keys():
					try:
						if name not in urls[url].keys(): 
							self.db.add_entry("Internet"," on ".join((name, url)),name,self.urls[url][name][0],url,self.urls[url][name][1],imageid=1,append=True)
					except:
						self.db.add_entry("Internet"," on ".join((name, url)),name,self.urls[url][name][0],url,self.urls[url][name][1],imageid=1,append=True)
	
	def save(self, file, password = ""):
		if file:
			if self.isKdb:
				if file[-4:] != ".kdb": file += ".kdb"
				self.sync_entries()
				self.db.write(str(file), str(password))
			else:
				#with open("urls", "w") as f:
				#	f.write('\n'.join((self.urls)))
				pass