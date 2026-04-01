# components/filters.py
import streamlit as st
from utils.data_loader import load_categories

def apply_sidebar_filters():
    st.sidebar.markdown("## 🔍 Filter Businesses")

    # Name search
    st.sidebar.markdown("**Search by name or keyword**")
    name = st.sidebar.text_input("", placeholder="e.g. coffee", label_visibility="collapsed")

    st.sidebar.markdown("---")

    # Category — fetched from API, falls back to empty list
    categories = load_categories()
    category = st.sidebar.selectbox("Category", [""] + categories)

    # City
    cities = ["All cities", "City Centre", "Benachity", "Durgapur", "Bidhan Nagar"]
    location = st.sidebar.selectbox("City", cities)
    # Normalise "All cities" → empty string so FastAPI ignores it
    if location == "All cities":
        location = ""

    # Rating
    st.sidebar.markdown("**Minimum rating ⭐**")
    rating = st.sidebar.slider("", 1.0, 5.0, 1.0, step=0.5, label_visibility="collapsed")

    return name, category, location, rating