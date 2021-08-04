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
