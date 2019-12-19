from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['deviceData']
test_collection = db['device']
print(test_collection)

