import unittest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
username = os.getenv('MONGODB_USERNAME')
userpassword = os.getenv('MONGODB_PASSWORD')

# Construct the MongoDB connection URL using credentials
mongourl = f"mongodb+srv://{username}:{userpassword}@cluster0.kshga.mongodb.net/"

class DatabaseReadTest(unittest.TestCase):
    """
    Unit test for MongoDB connection using the 'ping' command.
    Verifies that the application can connect to MongoDB successfully.
    """

    def setUp(self):
        """
        Set up MongoDB client before each test.
        """
        # Initialize MongoDB client
        self.client = MongoClient(mongourl)

    def test_mongodb_connection(self):
        """
        Test if the MongoDB client can connect to the database by pinging it.
        The test will pass if the ping command returns a response.
        """
        self.assertTrue(self.client.admin.command('ping'))  # Asserts that the 'ping' command is successful

    def tearDown(self):
        """
        Closes the MongoDB connection after the test is completed.
        This ensures there are no open connections left after running the test.
        """
        self.client.close()  # Close the client connection

if __name__ == '__main__':
    unittest.main()
