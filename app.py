import streamlit as st
from utils.data_loader import load_businesses
from components.hero import show_hero
from components.cards import show_business_cards
from components.filters import apply_sidebar_filters
from components.details import show_details

# ── Page config must come before ANY other st.* call ──────────────────────
# layout="wide" uses the full browser width instead of the narrow centre column.
st.set_page_config(page_title="Business Directory", layout="wide")


# ── Sidebar filters ────────────────────────────────────────────────────────
# Everything inside "with st.sidebar:" renders in the left panel.
# Streamlit auto-shows/hides the sidebar based on screen size
name, category, location, rating = apply_sidebar_filters()
# ── Fake business data ─────────────────────────────────────────────────────
# FastAPI now handles filtering, so we just pass the raw values through from the UI.
# Sidebar renders widgets and returns the chosen values
# Fetch businesses using those values (API or fallback)
businesses = load_businesses(name, category, location, rating)


# ── Hero banner ────────────────────────────────────────────────────────────
# st.markdown() lets you drop raw HTML into the page.
# unsafe_allow_html=True is required, otherwise Streamlit strips the tags.
show_hero()


# ── Business Cards ────────────────────────────────────────────────────────────
# st.columns() creates a horizontal layout. Here we make 3 equal-width columns.
show_business_cards(businesses)


# ── Business detail panel ──────────────────────────────────────────────────
# Check whether the user has clicked a "View details" button.
# session_state.get() returns None if the key doesn't exist yet,
# which is safe — we handle None with the `if selected_id:` check.
show_details()