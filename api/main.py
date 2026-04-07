from fastapi import FastAPI
from routes import auth, generate, payment, analytics

app = FastAPI()

app.include_router(auth.router)
app.include_router(generate.router)
app.include_router(payment.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"status": "API running"}
