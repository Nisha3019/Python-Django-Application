**Application Design and Development using Python and Django**

**Application Name - Django Traders**
It is a Python and Django-based application designed to manage customers and products with the following features:
  - Customer Model: Manage customer details (Create Read Update Delete operations).
  - Product Model: Manage product details (Create Read Update Delete operations).
  - CRUD Operations: Create, Read, Update, and Delete customers and products.
  - Search and Filter: Easily search and filter customers and products based information on specific criteria.
  - Visualizations & Graphs: Displays meaningful visualizations to analyze customer and product data.

**Installation in Visual Studio Code**
**Prerequisites**
Before proceeding, make sure to installed the following : 
  - Python (version 3.x): Download Python from https://www.python.org/downloads/
  - Django: This will be installed as part of the setup 
  - Visual Studio Code: Download VS Code from https://code.visualstudio.com/
  - VS Code Extensions: Python extension for VS Code

**Step-by-Step Guide**
1. Open the project folder 'DjangoTraders' in Visual Studio Code and Navigate into the project directory. (cd DjangoTraders)
2. Set up a Python virtual environment. (python3 -m venv venv)
3. Install the dependencies: (pip install -r requirements.txt)
4. Install VS Code extensions.
5. Run migrations: (python manage.py migrate)
6. Run the application: (python manage.py runserver)
7. Open a browser and navigate to http://127.0.0.1:8000/ to view the application.

**Functionality**

  **Customer & Product Models**
  - Create, Read, Update, and Delete (CRUD) operations for customer and product entries.
  - Each model contains essential fields (e.g., customer name, city, country, description, price for products, and product name, contact info for customers).

  **Search or Filter**
  - Easily search for customers or products based on their attributes (e.g., product name, customer name, city, country).
  - Filter products based on categories or price ranges.

  **Visualizations**
  -Visual graphs and charts to analyze customer and product data (e.g., annual sales, order placed, product purchased).

**Technologies Used**
  - Python 3.x
  - Django
  - SQLite (or any other database)
  - Plotly for visualizations
