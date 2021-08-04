from hug.middleware import CORSMiddleware
from pymongo import MongoClient
from bson.objectid import ObjectId
from formatters import *
from pprint import pprint
from urllib import parse
import hug, json

client = MongoClient()
db = client.test_db
api = hug.API(__name__)

api.http.add_middleware(CORSMiddleware(api, allow_origins=["*"]))

# GET
## by product
@hug.get("/products")
def get_all_products():
	return [format_product(p) for p in db.products.find()]

@hug.get("/product/{_id}")
def get_product_by_id(_id: hug.types.text):
	return format_product(db.products.find_one({"_id": ObjectId(_id)}))

## by category
@hug.get("/categories")
def get_all_categories():
	return [format_category(c) for c in db.categories.find()]

@hug.get("/category/{_id}")
def get_products_by_category(_id: hug.types.text):
	return [format_product(p) for p in db.products.find({"category_id": ObjectId(_id)})]

@hug.get("/category_name/{_id}")
def get_category_by_name(_id: hug.types.text):
	return format_category(db.categories.find_one({"_id": ObjectId(_id)}))


# POST

@hug.post("/new_product")
def new_product(p: hug.types.text):
	p = p.replace("\'", "\"")
	p = json.loads(p)
	# p = {category, name, price, description}
	db.products.insert_one({
		"category": p["category"],
		"category_id": db.categories.find_one({"name": p["category"]})["_id"],
		"name": p["name"],
		"price": p["price"],
		"description": p["description"]
	})

@hug.post("/update_product")
def update_product(new_p: hug.types.text):
	# new_p = {_id, category, category_id, name, price, description}
	new_p = new_p.replace("\'", "\"")
	new_p = json.loads(new_p)
	db.products.update_one({"_id": ObjectId(new_p["_id"])}, {"$set": {
		"category": new_p["category"],
		"category_id": ObjectId(new_p["category_id"]),
		"name": new_p["name"],
		"price": new_p["price"],
		"description": new_p["description"]
	}})

@hug.post("/new_category")
def new_category(name: hug.types.text):	
	db.categories.insert_one({"name": name})

# DELETE

@hug.delete("/delete_product/{_id}")
def delete_product(_id: hug.types.text):
	db.products.delete_one({"_id": ObjectId(_id)})

@hug.delete("/delete_category/{_id}")
def delete_category(_id: hug.types.text):
	db.products.delete_many({"category_id": ObjectId(_id)})
	db.categories.delete_one({"_id": ObjectId(_id)})
