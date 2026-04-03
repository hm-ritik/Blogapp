# 🚀 Blog Backend API (FastAPI + Docker)

## 📌 Project Overview

This is a production-ready backend for a blog application built using **FastAPI**.
It provides RESTful APIs to manage blog posts with proper project structure and Docker support.

### 🔧 Tech Stack

* FastAPI
* Python
* SQLite / PostgreSQL (optional)
* Docker & Docker Compose
* Uvicorn

---

## 📁 Project Structure

```
app/
 ├── api/routes/
 ├── core/
 ├── crud/
 ├── model/
 ├── schema/
 └── main.py
```

---

## ⚙️ Setup Instructions (Docker)

### 1. Clone the repository

```
git clone https://github.com/hm-ritik/Blogapp.git
cd Blogapp
```

### 2. Build and run using Docker

```
docker-compose up --build
```

### 3. Access the API

* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

---

## 📡 API Endpoints

### 📌 Get All Posts

```
GET /posts
```

### 📌 Get Single Post

```
GET /posts/{id}
```

### 📌 Create Post

```
POST /posts
```

### 📌 Update Post

```
PUT /posts/{id}
```

### 📌 Delete Post

```
DELETE /posts/{id}
```

---

## 📸 API Screenshots

### Get All Posts

![Get Posts](screenshots/get_posts.png)

### Create Post

![Create Post](screenshots/create_post.png)

### Get Single Post

![Get Single](screenshots/get_single.png)

---

## 🌍 Future Improvements

* Add JWT Authentication
* Add User System
* Deploy on cloud (Render / AWS)
* Add PostgreSQL

---

## 👨‍💻 Author

Ritik

