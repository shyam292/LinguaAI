# 🚀 LinguaAI

AI-powered language translation and grammar improvement web application built using **FastAPI**, **SQLite**, and **Ollama LLM (running locally)**.

---

## 🧠 Overview

LinguaAI is a full-stack AI language engine that:

- Translates text between languages
- Improves grammatically incorrect sentences
- Provides grammar scoring
- Stores translation history in a database
- Uses a locally running LLM via Ollama

This project demonstrates backend API design, database integration, frontend interaction, and AI model integration.

---

## 🔥 Features

- 🌍 Translate text between languages
- ✏️ Grammar correction with explanation
- 📊 Grammar scoring system
- 🗄️ Stores history in SQLite database
- ⚡ FastAPI backend (REST APIs)
- 🎨 HTML, CSS, JavaScript frontend
- 🤖 Integrated with Ollama LLM (local AI model)

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Ollama (LLM)

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📂 Project Structure

LinguaAI/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── ai_service.py # LLM integration
│ ├── database.py # DB connection setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # Database operations
│ ├── static/ # CSS & JS
│ └── templates/ # HTML frontend
│
├── .gitignore
└── README.md


---

## ⚙️ How It Works

1. User enters text in frontend.
2. JavaScript sends POST request to FastAPI backend.
3. Backend calls Ollama LLM locally.
4. LLM generates translation / correction.
5. Result is stored in SQLite database.
6. Response is returned to frontend.
7. UI updates dynamically without page reload.

---

## 🧪 API Endpoints

### 1️⃣ Translate Text
POST /translate


### 2️⃣ Improve Sentence
POST /ai/improve


---

## 💻 Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/LinguaAI.git
cd LinguaAI


### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Start Ollama

Make sure Ollama is installed and model is pulled:

ollama pull llama3
ollama run llama3


(Keep Ollama running locally)

### 5️⃣ Start FastAPI Server

uvicorn app.main:app --reload


Open in browser:
http://127.0.0.1:8000


---

## 📊 Database

- SQLite database is automatically created.
- Stores:
  - User ID
  - Source text
  - Translated text
  - Grammar score

---

## 🚀 Future Improvements

- User authentication
- Deployment on cloud
- Docker support
- Multiple LLM support
- Translation history dashboard

---

## 👨‍💻 Author

Shyam Ji Mishra  
BTech CSE (AI & ML)

---

## 📜 License

MIT License
