from pymongo import MongoClient
import pprint
from random import randint

# Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient()
db = client.ShoppingMindsSampleData
col = db.products

#1
name = db.products.find_one({}, {"_id": 0, "name": 1, "price": 1})
pprint.pprint(name)

#2
R = db.products.find_one({"name": { "$regex": "^R"}})
pprint.pprint(R)

#3 ik weet niet hoe
lst = []
for x in col.find({}, {"_id": 0, "price": 1}):
    lst.append(x)
pprint.pprint(lst)
