
# 🐳 Flask-RESTX + PostgreSQL CRUD API (Dockerized)

A lightweight Dockerized CRUD API built using **Flask-RESTX**, **SQLAlchemy**, and **PostgreSQL**, featuring pagination and JOIN queries.

## 🚀 Quick Start

### 1️⃣ Clone Repository
```bash
git clone https://github.com/bipindileepyadav-max/flask-postgres-crud-api.git
cd flask-postgres-crud-api
```

### 2️⃣ Build & Run Docker Containers
```bash
docker-compose up --build
```

### 3️⃣ Access the API
- Swagger UI → http://localhost:5000
- Base URL → http://localhost:5000/api

### 4️⃣ Stop Containers
```bash
docker-compose down
```

### 5️⃣ Run Command
Once the containers are up, you can interact with the API using `curl` or Postman.

For example, to **create a new customer**:
```bash
curl -X POST http://localhost:5000/api/customers   -H "Content-Type: application/json"   -d '{"name":"Bipin","email":"bipin@example.com"}'
```

### 6️⃣ Import Postman Collection
To easily test the API, you can import the **Postman Collection**:

1. Open **Postman** → Click **"Import"** (top-left).  
2. Select **"File"** → Upload the `postman_collection.json` file.  
3. Click **Import** → The collection will appear in your Postman sidebar.

You can now test all CRUD operations, including paginated GET requests and JOIN queries.

## 🧩 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| GET | /api/customers?page=1&per_page=5 | List customers (paginated) |
| POST | /api/customers | Add new customer |
| GET | /api/products?page=1&per_page=5 | List products (paginated) |
| POST | /api/products | Add new product |
| GET | /api/orders?page=1&per_page=5 | List orders (paginated) |
| POST | /api/orders | Create new order |
| GET | /api/orders/details?page=1&per_page=5 | View joined order details |

## 🧱 Tech Stack
- Flask-RESTX (API & Swagger)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Docker & Docker Compose (Containerization)

---
Made with using Python & Docker.
