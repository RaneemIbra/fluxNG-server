from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.documents_router import router as documents_router
from .api.users_router import router as users_router

app = FastAPI(title="FluxNG Engine", version="1.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents_router)
app.include_router(users_router)