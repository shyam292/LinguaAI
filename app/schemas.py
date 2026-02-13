from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str


class TranslationCreate(BaseModel):
    user_id: int
    source_text: str
    source_lang: str
    target_lang: str


class ImproveRequest(BaseModel):
    text: str

# Input Validation
# Agar client galat data bheje:
# {
#   "name": 123,
#   "email": "not-email"
# }

# FastAPI automatically 422 error de dega.

# manually check nahi karna padta.