# FastAPI + PostgreSQL CRUD API

A simple CRUD (Create, Read, Update, Delete) API built using FastAPI and PostgreSQL with SQLAlchemy.

---

## 🚀 Features

* Create a product
* Read all products
* Read a single product by ID
* Update a product
* Delete a product
* PostgreSQL database integration
* SQLAlchemy ORM support

---

## 🛠️ Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn

---

## 📁 Project Structure

```
.
├── main.py
├── database.py
├── models/
│   └── product.py        # Pydantic models
├── database_schemas/
│   └── product.py        # SQLAlchemy models
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install fastapi uvicorn sqlalchemy psycopg2
```

### 4. Setup PostgreSQL

* Make sure PostgreSQL is running
* Create a database
* Update your database connection in `database.py`

---

## ▶️ Run the Application

```
uvicorn main:app --reload
```

App will run at:

```
http://127.0.0.1:8000
```

---

## 📌 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/products`      | Get all products  |
| GET    | `/products/{id}` | Get product by ID |
| POST   | `/products`      | Add new product   |
| PUT    | `/products/{id}` | Update product    |
| DELETE | `/products/{id}` | Delete product    |

---

## 🧪 API Docs

Interactive API docs available at:

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🧠 Notes

* Initial product data is seeded automatically if the database is empty
* Uses dependency injection for database session management
* SQLAlchemy handles database operations

---

## 📄 License

This project is for learning purposes.
