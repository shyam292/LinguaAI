from fastapi import FastAPI, Depends
#FastAPI → app banane ke liye
#Depends → dependency injection ke liye (DB connection pass karne ke liye)

from sqlalchemy.orm import Session
#Session → database se baat karne ka object
#Ye ORM use karta hai SQL ke jagah Python se DB handle karne ke liye

from .database import engine, SessionLocal, Base
#Ye project ka database setup hai:
# engine → DB connection
# SessionLocal → har request ke liye DB session
# Base → models ke liye base class

from . import models, schemas, crud, ai_service
from .logger import logger
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


Base.metadata.create_all(bind=engine)
# DB me tables create karta hai
# Jo models.py me defined hain unke according
# Simple words: Agar table nahi hai → bana do

app = FastAPI(title="LinguaAI – AI Language & Grammar Engine")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# CSS, JS,Images
# Serve karta hai frontend ke liye.
# Example:localhost:8000/static/style.css

templates = Jinja2Templates(directory="app/templates")
# Ye HTML templates render karne ke liye use hota hai.
# Matlab: Backend → HTML generate karta hai → Browser ko bhejta hai.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🧩 Step by Step Flow
# 1️⃣ Request aayi
# 2️⃣ FastAPI ne get_db() call kiya
# 3️⃣ db = SessionLocal() run hua
# 4️⃣ yield db → control route ko mil gaya

# Ab route ka code execute hota hai.

# 5️⃣ Route complete hua
# 6️⃣ FastAPI generator resume karta hai
# 7️⃣ finally block run hota hai
# 8️⃣ db.close() execute


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("Creating user")
    return crud.create_user(db, user.name, user.email)
# Jab request aati hai: FastAPI dekhta hai Depends(get_db): Wo get_db() function ko call karta hai
# SessionLocal() run hota hai: Ek naya DB session create hota hai
# Matlab: Har API request → apna separate DB connection
# Ye concurrency ke liye important hai.

# schemas.UserCreate: Ye Pydantic model hota hai.


@app.post("/translate")
def translate(data: schemas.TranslationCreate, db: Session = Depends(get_db)):

    translate_prompt = f"""
Translate this sentence to {data.target_lang}.

Sentence:
{data.source_text}

Only return the translated sentence.
If the language is Hindi, return the answer in Hindi script.
"""

    translated_text = ai_service.generate_response(translate_prompt)

    grammar_prompt = f"""
Give grammar score out of 10 as a decimal number only.
Do not explain.
Just return a number like 7.5

Sentence: {data.source_text}
"""

    grammar_score_raw = ai_service.generate_response(grammar_prompt)

    try:
        grammar_score = float(grammar_score_raw.strip().split()[0])
    except:
        grammar_score = 0.0

    record = {
        "user_id": data.user_id,
        "source_text": data.source_text,
        "translated_text": translated_text,
        "source_lang": data.source_lang,
        "target_lang": data.target_lang,
        "grammar_score": grammar_score
    }

    return crud.create_translation(db, record)


@app.post("/ai/improve")
def improve(req: schemas.ImproveRequest):

    prompt = f"""
    Correct grammar and improve this sentence.
    Also provide grammar score out of 10.

    Sentence: {req.text}
    """

    result = ai_service.generate_response(prompt)

    return {"result": result}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
