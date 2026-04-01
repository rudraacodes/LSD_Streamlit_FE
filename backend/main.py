from fastapi import FastAPI
from backend.database import init_db
from backend.routers import businesses, categories

app = FastAPI(title="LSD API")

# Create tables + seed data when the server starts
@app.on_event("startup")
def startup():
    init_db()

# Register routers
app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(businesses.router, prefix="/api/businesses", tags=["businesses"])

# Health check — useful to confirm the server is alive
@app.get("/")
def root():
    return {"status": "LSD API is running"}