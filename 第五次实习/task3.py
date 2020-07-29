import pymongo
from pymongo import MongoClient
import json

if __name__ == '__main__':
	country_dict = {}
	collection = MongoClient()['DB5'].data

	record_set = collection.find()
	for record in record_set:
		authors = record['metadata']['authors']
		for author in authors:
			if "affiliation" in author.keys():
				affiliation = author['affiliation']
				if "location" in affiliation.keys():
					location = affiliation['location']
					if "country" in location.keys():
						country = location['country']
						if country == "P. R. China":
							country = "China"
						if country == "People's Republic of China":
							country = "China"
						if country == "China, China":
							country = "China"
						if country == "United States":
							country = "USA"
						if country == "United Kingdom":
							country = "UK"
						if country in country_dict.keys():
							country_dict[country] += 1
						else:
							country_dict[country] = 1
	sort_dict = sorted(country_dict.items(), key = lambda kv: (kv[1], kv[0]), reverse = True)
	for i in range(15):
		print(sort_dict[i])



