import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('MONGODB_USERNAME')
userpassword = os.getenv('MONGODB_PASSWORD')
mongourl=f"mongodb+srv://{username}:{userpassword}@cluster0.kshga.mongodb.net/"

client = MongoClient(mongourl)
db = client.shop_db
products_collection = db.products

class DatabaseReadTest(unittest.TestCase):
    def test_mongodb_connection(self):
        client = MongoClient(mongourl)
        self.assertTrue(client.admin.command('ping'))

    def tearDown(self):
        # Close the connection after the test is done
        self.client.close()

if __name__ == '__main__':
    unittest.main()
