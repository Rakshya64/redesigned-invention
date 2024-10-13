from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://rakchya64d:Sry85NbqqZttrTnW@cluster0.kshga.mongodb.net/")
db = client.shop_db
products_collction = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Fetch all products from MongoDB
    all_products = products_collction.find()
    return render_template('products.html', products=all_products)

if __name__ == '__main__':
    app.run(debug=True)


