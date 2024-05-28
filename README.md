## Project Description: E-commerce Product Listing and Filtering Application

### Overview

This project is an e-commerce web application designed to list and filter products dynamically. Built with Vue 3, Vite, Pinia for state management, and Tailwind CSS for styling, the application interacts with a Django backend to fetch and display product data. The primary features include product listing, category filtering, search functionality, and pagination.

### Key Features

1. **Product Listing**:
   - Display a grid of products with details such as title, description, price, and images.
   - Each product card shows the primary image and essential information about the product.

2. **Category Filtering**:
   - A sidebar with a list of categories, each with a checkbox to filter products.
   - Users can select multiple categories to filter the product list dynamically.
   - Includes a dropdown in the search bar for quick category selection.

3. **Search Functionality**:
   - A search bar that allows users to search for products by name.
   - Integrates with category filters to refine search results within selected categories.

4. **Pagination**:
   - Pagination controls to navigate through multiple pages of products.
   - Displays a limited number of products per page, with controls to move to the next or previous page.

5. **Clear Filters**:
   - A button to clear all selected filters and reset the product list to its initial state.

### Technical Details

- **Frontend**:
  - **Vue 3**: Utilized for building a reactive and component-based user interface.
  - **Vite**: Used for fast and efficient build tooling.
  - **Pinia**: State management library used to manage the application's state, particularly for product data and filters.
  - **Tailwind CSS**: A utility-first CSS framework for styling the application.

- **Backend**:
  - **Django**: Serves as the backend framework, providing APIs for fetching product data.
  - **Django REST Framework**: Used to create APIs for product listing and category data.
  - **Models**: `Product` and `ProductResource` models are defined to handle product details and associated images.

### Code Structure

1. **Django Models**:
   - `Product`: Represents the product details.
   - `ProductResource`: Represents the images associated with each product.

2. **Django Serializers**:
   - `ProductSerializer`: Serializes product data along with associated images.
   - `ProductResourceSerializer`: Serializes image data for products.

3. **Django Views**:
   - `product_list`: API view to retrieve a list of products.

4. **Vue Components**:
   - `ProductList.vue`: Displays a list of products.
   - `CategoryFilter.vue`: Renders category checkboxes and a clear filters button.
   - `SearchBar.vue`: Includes a search input and category dropdown.
   - `Pagination.vue`: Provides pagination controls.

5. **State Management (Pinia)**:
   - `productStore.js`: Manages product data, filters, and search queries.

6. **HTTP Utilities**:
   - `request_http.js`: Defines functions for making GET and POST requests using Axios.

### Usage

1. **Setup**:
   - Clone the repository.
   - Install dependencies for both the frontend and backend.

2. **Backend**:
   - Run Django migrations to set up the database.
   - Start the Django development server.

3. **Frontend**:
   - Start the Vite development server.
   - Access the application in a web browser.

### Conclusion

This project demonstrates a comprehensive e-commerce solution with dynamic product listing, filtering, and searching capabilities. It leverages modern web technologies to create an efficient and user-friendly interface for browsing products.

### How to Run the Project

## Clone the repository:
```bash
git clone https://github.com/carlos18bp/catalog_feature.git
cd catalog_feature
```

## Install virtualenv:
```bash
pip install virtualenv
```

## To create a new virtual env:
```bash
virtualenv name_virtual_env
```

## Create virtual env:
```bash
virtualenv catalog_feature_env
```

## Activate virtual env:
```bash
source catalog_feature_env/bin/activate
```

## Create dependencies file:
```bash
pip freeze > requirements.txt
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Desactivate virtual env:
```bash
deactivate
```

## Run makemigrations:
```bash
python3 manage.py makemigrations
```

## Run migrations:
```bash
python3 manage.py migrate
```

## Create superuser:
```bash
python3 manage.py createsuperuser
```

## Start the server:
```bash
python3 manage.py runserver
```

## Frontend setup:
```bash
cd frontend
npm install
npm run dev
```