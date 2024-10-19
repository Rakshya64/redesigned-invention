from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
username=os.getenv('MONGODB_USERNAME')
userpassword =os.getenv('MONGODB_PASSWORD')

app = Flask(__name__)
mongourl=f"mongodb+srv://{username}:{userpassword}@cluster0.kshga.mongodb.net/"

client = MongoClient(mongourl)
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


