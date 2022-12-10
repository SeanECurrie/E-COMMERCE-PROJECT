from app import app
from flask import render_template
import requests

def get_driver_info(productName):
    productData = []

@app.route('/')
@app.route('/home')
def home():
    allProducts = 'https://fakestoreapi.com/products'
    getAllProducts = requests.get(allProducts)
    productName = getAllProducts.json()[2]
    i = 0

    results = []

    for product in getAllProducts:
        name = getAllProducts.json()[i]['title']
        price = getAllProducts.json()[i]['price']
        description = getAllProducts.json()[i]['description']
        category = getAllProducts.json()[i]['category']
        image = getAllProducts.json()[i]['image']
        rating = getAllProducts.json()[i]['rating']

        productInfo = {
            'id': i,
            'name': name,
            'price': price,
            'description': description,
            'category': category,
            'image': image,
            'rating': rating
            }
        i += 1
        results.append(productInfo)
        if i > 19:
            return render_template('index.html', results=results)


@app.route('/product/<int:id>')
def productView(id):
    allProducts = 'https://fakestoreapi.com/products'
    getAllProducts = requests.get(allProducts)
    productName = getAllProducts.json()[2]

    name = getAllProducts.json()[id]['title']
    price = getAllProducts.json()[id]['price']
    description = getAllProducts.json()[id]['description']
    category = getAllProducts.json()[id]['category']
    image = getAllProducts.json()[id]['image']
    rating = getAllProducts.json()[id]['rating']

    return render_template('single-product-view.html', name=name, price=price, description=description, category=category, image=image, rating=rating)