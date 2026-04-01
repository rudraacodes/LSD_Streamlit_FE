import httpx

BASE_URL = "http://localhost:8000"

def get_businesses(name="", category="", location="", min_rating=0.0):
    params = {
        "name":       name,
        "category":   category,
        "location":   location,
        "min_rating": min_rating,
    }
    try:
        response = httpx.get(f"{BASE_URL}/api/businesses/", params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError:
        return []   # FastAPI is not running — return empty gracefully

def get_categories():
    try:
        response = httpx.get(f"{BASE_URL}/api/categories/", timeout=30)
        response.raise_for_status()
        return [cat["name"] for cat in response.json()]
    except httpx.RequestError:
        return []