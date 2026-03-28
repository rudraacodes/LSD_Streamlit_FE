import streamlit as st
from utils.data_loader import load_businesses
from components.hero import show_hero
from components.cards import show_business_cards
from components.filters import apply_sidebar_filters
from components.details import show_details

# ── Page config must come before ANY other st.* call ──────────────────────
# layout="wide" uses the full browser width instead of the narrow centre column.
st.set_page_config(page_title="Business Directory", layout="wide")

# ── Fake business data ─────────────────────────────────────────────────────
# This is just a Python list of dicts. Later you'd replace this with
# a real API call. For now, it lets you build the whole UI without a backend.
# Load data
businesses = load_businesses()

# ── Hero banner ────────────────────────────────────────────────────────────
# st.markdown() lets you drop raw HTML into the page.
# unsafe_allow_html=True is required, otherwise Streamlit strips the tags.
show_hero()

# ── Business Cards ────────────────────────────────────────────────────────────
# st.columns() creates a horizontal layout. Here we make 3 equal-width columns.
show_business_cards(businesses)

# ── Sidebar filters ────────────────────────────────────────────────────────
# Everything inside "with st.sidebar:" renders in the left panel.
# Streamlit auto-shows/hides the sidebar based on screen size.
show_filters = apply_sidebar_filters(businesses)

# ── Business detail panel ──────────────────────────────────────────────────
# Check whether the user has clicked a "View details" button.
# session_state.get() returns None if the key doesn't exist yet,
# which is safe — we handle None with the `if selected_id:` check.
show_details()