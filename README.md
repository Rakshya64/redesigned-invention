# Flask MongoDB Application with CI/CD

This project is a Flask application that interacts with a MongoDB database, 
featuring routes for a homepage and a products page. 
The application includes a CI/CD pipeline configured in GitHub Actions 
to automatically test the code on every push to the `main` branch.

# Project Structure

- "app": Contains the main application code, including routes, templates, and database configuration.
- "tests": Contains unit tests for routes and database operations.
- ".github/workflows/ci.yml": GitHub Actions configuration file for CI/CD.

# Environment Setup

1. Clone the repository:
  
   git clone <repository-url>
   
2. Install dependencies:
   
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   
3. Environment Variables: Set up environment variables in a `.env` file:
   
   MONGODB_USERNAME
   MONGODB_PASSWORD
   

# Unit Tests

The application includes three main unit tests to verify route and database functionality:

1. Route Test - Invalid Method for Home Route:
   - Purpose: Ensures that the '/' (home) route only allows the correct HTTP method (GET).
   - Test Details: Sends a POST request to the '/' route and expects a '405 Method Not Allowed' status.

2. Database Connection Test - MongoDB Read Operation:
   - Purpose: Verifies the application can connect to MongoDB by "pinging" the database.
   - Test Details: Uses 'pymongo' to check the database connection. If the connection fails, the test fails.

3. Database Write Test - MongoDB Insert Operation:
   - Purpose: Tests if a document can be inserted into the MongoDB collection.
   - Test Details: Inserts a sample document into the 'products' collection and checks if it is correctly added by querying for the document.

# CI/CD Pipeline

The CI/CD pipeline is configured to run automatically on every push to the 'main' branch. 
It performs the following steps:

1. Checkout Code: Pulls the code from the repository.
2. Set Up Python: Installs Python 3.11 on the runner.
3. Install Dependencies: Installs the required Python packages.
4. Run Unit Tests: Runs the unit tests located in the 'tests' directory.





   

