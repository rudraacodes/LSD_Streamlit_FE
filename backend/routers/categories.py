from fastapi import APIRouter
from backend.database import get_connection

router = APIRouter()

@router.get("/")
def get_categories():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM categories ORDER BY name").fetchall()
    conn.close()
    return [dict(row) for row in rows]