# 🚀 NEXUS – Event Registration System

A futuristic **event registration web application** built using **Flask + MongoDB + Vanilla JS**.

Users can register for university events through a modern UI, and all data is stored securely in MongoDB.

---

## 📌 Features

* 🔥 Interactive UI (cyberpunk themed)
* 📝 Event registration form
* 📦 Backend API using Flask
* 🗄️ MongoDB database integration
* 📊 Admin APIs (view registrations & stats)
* ⚡ Real-time validation
* 🎉 Success animation after registration

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask) 
* **Database:** MongoDB
* **Others:** Flask-CORS, PyMongo

---

## 📁 Project Structure

```
project-root/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

Make sure you have installed:

* Python (>= 3.8)
* MongoDB (running locally)
* pip (Python package manager)

---

## 📦 Installation Steps

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/nexus-registration.git
cd nexus-registration
```

---

### 2️⃣ Install dependencies

```bash
pip install flask flask-cors pymongo
```

OR (recommended)

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Start MongoDB

Make sure MongoDB is running on:

```
mongodb://localhost:27017/
```

Database used:

```
nexus_db
```

Collection:

```
registrations
```

---

### 4️⃣ Run the Flask server

```bash
cd backend
python app.py
```

Server will start at:

```
http://localhost:5000
```

---

### 5️⃣ Open the application

Open browser and go to:

```
http://localhost:5000
```

---

## 🔌 API Endpoints

### ✅ Register User

```
POST /api/register
```

**Body:**

```json
{
  "full_name": "John Doe",
  "student_id": "GLS2024001",
  "email": "john@example.com",
  "event_id": "TECHFEST-26",
  "event_name": "Tech Fest 2026"
}
```

---

### 📋 Get All Registrations

```
GET /api/registrations
```

---

### 📊 Get Stats

```
GET /api/stats
```

---

### ❤️ Health Check

```
GET /api/health
```

---

## ⚠️ Important Notes

* MongoDB must be running before starting backend
* Backend runs on port **5000**
* Frontend is served by Flask (no separate server needed)
* CORS is already enabled

---

## 🧠 How It Works

1. User fills form on frontend 
2. Data is sent to Flask API (`/api/register`)
3. Backend validates input
4. Data is stored in MongoDB
5. Unique registration ID is generated
6. Success response is shown on UI

---

## 🔧 Improvements (Optional)

* Add authentication (Admin login)
* Deploy on cloud (Render / Railway / AWS)
* Add email confirmation
* Add Docker support
* Add `.env` for config

---

## 🧑‍💻 Author

**Rishabh** **Granth**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
