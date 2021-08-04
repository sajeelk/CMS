def format_product(p):
	return {
		"_id": str(p["_id"]),
		"category": p["category"],
		"category_id": str(p["category_id"]),
		"name": p["name"],
		"price": p["price"],
		"description": p["description"]
	}

def format_category(c):
	return {
		"_id": str(c["_id"]),
		"name": c["name"]
	}
