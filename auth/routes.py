from fastapi import APIRouter, HTTPException
from db.database import SessionLocal
from db.models import User
from auth.auth_utils import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/signup")
def signup(email: str, password: str):
    db = SessionLocal()

    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.close()

    return {"message": "User created successfully"}


@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }