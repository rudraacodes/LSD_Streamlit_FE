from fastapi import APIRouter, Query
from backend.database import get_connection

router = APIRouter()

@router.get("/")
def get_businesses(
    name:       str   = Query(default=""),
    category:   str   = Query(default=""),
    location:   str   = Query(default=""),
    min_rating: float = Query(default=0.0)
):
    conn = get_connection()

    query  = "SELECT * FROM businesses WHERE is_active = 1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if category:
        query += " AND category = ?"
        params.append(category)
    if location:
        query += " AND location = ?"
        params.append(location)
    if min_rating > 0:
        query += " AND rating >= ?"
        params.append(min_rating)

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]