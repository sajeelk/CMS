from flask import *
import requests
app = Flask(__name__)

api_base = "http://localhost:8000"


@app.route('/')
def index():
	r = requests.get(api_base + "/categories")
	return render_template("index.html", categories=r.json())

@app.route('/category/<_id>')
def category_view(_id):
	r = requests.get(api_base + "/category/%s" % _id)
	c = requests.get(api_base + "/category_name/%s" % _id)
	return render_template("category_view.html", products=r.json(), c=c.json())

@app.route('/product/<_id>')
def product_view(_id):
	r = requests.get(api_base + "/product/%s" % _id)
	return render_template("product_view.html", p=r.json())

@app.route('/update_product/<_id>')
def product_edit(_id):
	r = requests.get(api_base + "/product/%s" % _id).json()
	return render_template("product_edit.html", p=r, c={"_id": r["category_id"], "name": r["category"]})

@app.route('/new_product/<_id>')
def new_product(_id):
	c = requests.get(api_base + "/category_name/%s" % _id).json()
	return render_template("new_product.html", c=c)

@app.route('/delete_category/<_id>')
def delete_category(_id):
	requests.delete(api_base + "/delete_category/%s" % _id)
	return redirect(url_for('index'))

@app.route('/delete_product/<_id>')
def delete_product(_id):
	c_id = requests.get(api_base + "/product/%s" % _id).json()["category_id"]
	requests.delete(api_base + "/delete_product/%s" % _id)
	return redirect(url_for('category_view', _id=c_id))

