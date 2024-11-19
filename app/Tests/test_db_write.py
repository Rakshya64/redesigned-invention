import unittest
from pymongo import MongoClient
from app import app, products_collction  # Import your Flask app and MongoDB collection


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Flask test client and MongoDB collection for testing
        self.client = app.test_client()
        self.db = products_collction  # Use the collection defined in your Flask app

    def test_write_data_to_db(self):
        # Define new data to insert
        new_data = {"field": "new_value"}

        # Insert the data into the MongoDB collection
        insertion_result = self.db.insert_one(new_data)

        # Use assertions to ensure the document was inserted
        # Verify the insertion result contains an ObjectId, indicating a successful insert
        self.assertIsNotNone(insertion_result.inserted_id, "Document was not successfully inserted.")

        # Query the database to check the data’s presence
        inserted_data = self.db.find_one({"field": "new_value"})

        # Assertions to check that the document is present and has the expected content
        self.assertIsNotNone(inserted_data, "Inserted data is not found in the database.")
        self.assertEqual(inserted_data["field"], "new_value", "The inserted data does not match the expected value.")

        # Clean up: Delete the inserted document to keep the test isolated
        self.db.delete_one({"field": "new_value"})


if __name__ == '__main__':
    unittest.main()
