import pymongo
from pymongo import MongoClient
import json

if __name__ == '__main__':
	abstract_dict = {}
	abandon_list = {"of", "in", "on", "From", "by", "The", "the", "a", "A", "for", "with", "to", "be","been", "is", "and", ",", ".", "?", "1", "2","3","that","were","was","from","we","We","are","is","this","these","an","not","or","has","at","which","when","what","as","have","can","In","between"}
	collection = MongoClient()['DB5'].data

	record_set = collection.find()
	for record in record_set:
		abstracts = record['abstract']
		for i in abstracts:
			abstract = i['text']
			words = abstract.split(" ")
			for word in words:
				if word not in abandon_list:
					if word in abstract_dict.keys():
						abstract_dict[word] += 1
					else:
						abstract_dict[word] = 1
	sort_dict = sorted(abstract_dict.items(), key = lambda kv:(kv[1],kv[0]), reverse = True)
	for i in range(15):
		print(sort_dict[i])



