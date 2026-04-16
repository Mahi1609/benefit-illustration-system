from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from api.routes.policy import router as policy_router
from db.database import engine, Base
from auth.routes import router as auth_router

app = FastAPI(
    title="Benefit Illustration API",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/auth")

templates = Jinja2Templates(directory="templates")

app.include_router(policy_router, prefix="/policy")



Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}

# print(type(templates))

# @app.get("/")
# def serve_ui(request: Request):
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request}
#     )

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {
        "app": "Benefit Illustration API",
        "version": "1.0.0",
        "description": "Insurance policy benefit calculation engine"
    }


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})