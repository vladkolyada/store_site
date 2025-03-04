# Store Site – Computer Hardware Online Store

Store Site is a web application designed for an online computer hardware store. It allows users to browse a catalog of computer products, view detailed information about each item, and manage their shopping cart.

## Website Features

### 1. Home Page (/)

* Displays featured products and promotions.
* Provides navigation to product categories and other sections.

### 2. Product Catalog (/products)

* Lists all available products with basic information:
  * Product name
  * Short description
  * Price
* Allows filtering and sorting by categories, price, and other attributes.

### 3. Product Detail Page (/products/<product_id>)

* Provides detailed information about a selected product:
  * High-resolution images
  * Full description
  * Specifications
  * Customer reviews

### 4. Shopping Cart (/cart)

* Displays products added to the cart with quantities and total price. 
* Allows updating quantities or removing products.

### 5. Checkout Process (/checkout)

* Collects shipping and payment information.
* Processes orders and provides confirmation.

### 6. User Authentication

* Registration (/register)
* Login (/login)
* Profile management (/profile)

## Technologies Used
* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLAlchemy

## For Developers

This project is a web application built with Flask. It includes a basic structure for web applications, covering settings, routing, models, and templates.

### Project Structure

* `app/` – Main application directory containing:

  * `__init__.py` – Initializes the Flask application.

  * `routes.py` – Defines URL routes and their corresponding view functions.

  * `models.py` – Contains database models.

  * `templates/` – HTML templates.

  * `static/` – Static files (CSS, JS, images).

* `instance/` – Contains configuration files and the SQLite database.

* `migrations/` – Database migration files.

* `venv/` – Python virtual environment.

* `README.md` – Project documentation.

## Installation & Setup

### 1. Clone the repository

`git clone https://github.com/vladkolyada/store_site.git`

`cd store_site`

### 2. Create and activate a virtual environment

`python -m venv venv`
`source venv/bin/activate  # On Windows: venv\Scripts\activate`

### 3. Install dependencies

`pip install -r requirements.txt`

### 4. Set up the database

`flask db upgrade`

### 5. Run the application

`flask run`

### 6. Open in a browser

Visit http://127.0.0.1:5000/ to access the site.

Note: Ensure that you have Python and Flask installed on your system. For detailed instructions, refer to the official Flask documentation.
