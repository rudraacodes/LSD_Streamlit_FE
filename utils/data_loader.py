# utils/data_loader.py
from utils.api_client import get_businesses, get_categories

FALLBACK_BUSINESSES = [
    {"name": "Chai Stop",        "category": "Restaurant",     "location": "City Centre", "rating": 4.5},
    {"name": "Glow Salon",       "category": "Salon",          "location": "Benachity",   "rating": 4.0},
    {"name": "BuildRight",       "category": "Hardware Store", "location": "Durgapur",    "rating": 3.5},
    {"name": "MedPlus Pharmacy", "category": "Pharmacy",       "location": "City Centre", "rating": 4.5},
    {"name": "IronZone Gym",     "category": "Gym",            "location": "Bidhan Nagar","rating": 4.5},
]

FALLBACK_CATEGORIES = ["Restaurant", "Salon", "Hardware Store", "Pharmacy", "Gym"]

def load_businesses(name="", category="", location="", min_rating=0.0):
    result = get_businesses(name, category, location, min_rating)
    if result:
        return result
    # FastAPI not running — use mock data with manual filtering
    data = FALLBACK_BUSINESSES
    if name:
        data = [b for b in data if name.lower() in b["name"].lower()]
    if category:
        data = [b for b in data if b["category"] == category]
    if location:
        data = [b for b in data if b["location"] == location]
    if min_rating > 0:
        data = [b for b in data if b["rating"] >= min_rating]
    return data

def load_categories():
    result = get_categories()
    return result if result else FALLBACK_CATEGORIES