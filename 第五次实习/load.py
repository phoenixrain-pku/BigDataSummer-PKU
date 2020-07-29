import pymongo
import os.path
import json
from pymongo import MongoClient
from pymongo import InsertOne

class data_loader(object):
	def __init__(self):
		self.host = "localhost"
		self.port = 27107

	def loading(self,dirpath):
		
		connection = MongoClient('localhost')
		self.db = connection.demo01
		# create a DB instance
		self.client = MongoClient()

		#create collection
		self.collection = self.client.DB5.data

		#open file and load
		dir = os.listdir(dirpath)
		wrong = 0
		for jsonname in dir:
			file = open(dirpath + "/" + jsonname,'r')
			jsondata = json.load(file)
			try:
				self.collection.insert(jsondata)
				print("succeed in file:{}".format(jsonname))
			except:
				print("wrong in file:{}".format(jsonname))
				wrong = wrong + 1
			file.close()
		print("wrong file:{}".format(wrong))

if __name__ == '__main__':
	loader = data_loader()
	loader.loading("CORD-19-research")

