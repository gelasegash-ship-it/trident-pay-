from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.auth import router as auth_router
from backend.upload import router as upload_router
from backend.payment import router as payment_router

app = FastAPI(title="TRIDENT PAY API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(auth_router, prefix="/api/auth")
app.include_router(upload_router, prefix="/api")
app.include_router(payment_router, prefix="/api/payment")
@app.get("/")
def root(): return {"status": "TRIDENT PAY API is running"}
