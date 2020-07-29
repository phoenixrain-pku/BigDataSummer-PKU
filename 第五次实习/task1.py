import pymongo
from pymongo import MongoClient
import json

if __name__ == '__main__':
	title_dict = {}
	abandon_list = {"of", "in", "on", "From", "by", "The", "the", "a", "A", "for", "with", "to", "be", "is", "and", ",", ".", "?", "1", "2","3"}
	collection = MongoClient()['DB5'].data

	record_set = collection.find()
	for record in record_set:
		title = record['metadata']['title']
		words = title.split(" ")
		for word in words:
			if word not in abandon_list:
				if word in title_dict.keys():
					title_dict[word] += 1
				else:
					title_dict[word] = 1
	sort_dict = sorted(title_dict.items(), key = lambda kv:(kv[1],kv[0]), reverse = True)
	for i in range(10):
		print(sort_dict[i])



