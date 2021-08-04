from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.test_db

def drop():
	client.drop_database('test_db')

def populate():
	cat_ids = db.categories.insert_many([
		{ "name": "Juice" },
		{ "name": "Water" },
		{ "name": "Chips" }]).inserted_ids
	db.products.insert_many([
		{ "category": "Juice", "category_id": cat_ids[0], "name": "Shezan Mango Juice", "price": 700, "description": "The best mango juice you'll taste" },
		{ "category": "Juice", "category_id": cat_ids[0], "name": "Maaza Mango Drink", "price": 500, "description": "The mango juice thats trying to be as good as Shezan but just can't" },
		{ "category": "Juice", "category_id": cat_ids[0], "name": "Dabur Mango Drink", "price": 300, "description": "Honestly never tried it so I really just don't know" },
		{ "category": "Water", "category_id": cat_ids[1], "name": "Icelandic Water", "price": 500, "description": "The best water you'll taste" },
		{ "category": "Water", "category_id": cat_ids[1], "name": "Evian Water", "price": 300, "description": "Pretty decent, just not as good as Icelandic water" },
		{ "category": "Water", "category_id": cat_ids[1], "name": "Deer Park Water", "price": 100, "description": "Probably the best choice, pretty cheap and who cares what water you drink anyway" },
		{ "category": "Chips", "category_id": cat_ids[2], "name": "Flaming Hot Cheetos", "price": 900, "description": "The best spicy chip, only problem is red fingertips" },
		{ "category": "Chips", "category_id": cat_ids[2], "name": "Takis", "price": 850, "description": "Almost as good as Cheetos, but they are hard to eat with friends because of the spice level and excessively red fingers" },
		{ "category": "Chips", "category_id": cat_ids[2], "name": "Cape Cod Jalapeno Chips", "price": 900, "description": "Most ideal to eat in public, still pretty amazing too" }])