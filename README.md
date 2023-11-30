# Vendor Management System with Performance Metrics

This Django application serves as a Vendor Management System (VMS) with features to manage vendor profiles, track purchase orders, and calculate performance metrics for vendors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
   git clone https://github.com/ashikos/Vendor-Management-System.git

## navigate to the project directory:
cd vendor-management-system


## Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


## Install the project dependencies:
pip install -r requirements.txt


## Apply database migrations:
python manage.py migrate


## Create a superuser to access the Django admin:
python manage.py createsuperuser


Start the development server:
python manage.py runserver



## Usage
The Vendor Management System provides APIs to manage vendors and track purchase orders. Detailed documentation for API endpoints and data models can be found in the API Endpoints section below


API Endpoints

    All the APIs except Singnup, login are secured by Jwt Authentication.
    User need to singup and login inorder to access all other Endpoints.
    A JWT token is received after the succefull login, these tokens sholud be saved in the cookies in order to 
    acccess other api Endpoints.
   
    Swagger: All apis are documented using swagger
        /api/swagger/ 
    
    Authentication:
        POST /api/accounts/signup/ : create a new user
        POST /api/accounts/login/ : login api which generates a jwt token which should be attached in cookies.
        GET /api/accounts/user/ : get details of logged user
        POST /api/accounts/logout/ : logout api 

    Vendor Profile Management:
        POST /api/vendors/: Create a new vendor.
        GET /api/vendors/: List all vendors.
        GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
        PUT /api/vendors/{vendor_id}/: Update a vendor's details.
        DELETE /api/vendors/{vendor_id}/: Delete a vendor.

    Purchase Order Tracking:
        POST /api/purchase_orders/: Create a purchase order.
        GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
        GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
        PUT /api/purchase_orders/{po_id}/: Update a purchase order.
        DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

    Vendor Performance Evaluation:
        GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.





