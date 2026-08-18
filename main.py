from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import auth, upload, payment

app = FastAPI(title="API TRIDENT PAY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(payment.router)

@app.get("/")
def root():
    return {"statut": "L'API TRIDENT PAY FONCTIONNE"}
