# filters.py
# NOTE: Filtering is now handled by FastAPI (backend/routers/businesses.py)
# This file is no longer called. Kept for reference.

import streamlit as st

def apply_sidebar_filters(BUSINESSES):

    # ── Sidebar filters ────────────────────────────────────────────────────────
    with st.sidebar:
        st.header("🔍 Filter Businesses")

        query = st.text_input("Search by name or keyword", placeholder="e.g. coffee")

        st.divider()

        all_categories = sorted(set(b["category"] for b in BUSINESSES))
        sel_categories = st.multiselect("Category", all_categories)

        all_cities = ["All cities"] + sorted(set(b["city"] for b in BUSINESSES))
        sel_city = st.selectbox("City", all_cities)

        min_rating = st.slider(
            "Minimum rating ⭐",
            min_value=1.0,
            max_value=5.0,
            value=1.0,
            step=0.5
        )

    # ── Filtering logic ────────────────────────────────────────────────────────
    # This runs EVERY time the user changes any control above.
    # Streamlit re-runs the whole script from top to bottom on each interaction,
    # so `results` always reflects the current state of the sidebar widgets.
    results = BUSINESSES

    if query:
        results = [b for b in results
                   if query.lower() in b["name"].lower()
                   or query.lower() in b["desc"].lower()]

    if sel_categories:
        results = [b for b in results if b["category"] in sel_categories]

    if sel_city != "All cities":
        results = [b for b in results if b["city"] == sel_city]

    results = [b for b in results if b["rating"] >= min_rating]

    st.subheader(f"Showing {len(results)} business{'es' if len(results) != 1 else ''}")

    # ── Business card grid ─────────────────────────────────────────────────────
    # Show a message if no businesses matched the filters
    if not results:
        st.info("No businesses match your filters. Try loosening the criteria.")

    # st.columns(3) splits the page into 3 equal columns.
    # It returns a list of column objects — cols[0], cols[1], cols[2].
    # We cycle through them using i % 3 so card 0 → col 0, card 1 → col 1,
    # card 2 → col 2, card 3 → col 0 again, and so on.
    cols = st.columns(3, gap="medium")

    for i, biz in enumerate(results):
        with cols[i % 3]:

            # st.container(border=True) draws a rounded card with a border.
            # Everything indented under "with container:" goes inside that card.
            with st.container(border=True):

                # Top row: business name + star rating side by side
                name_col, rating_col = st.columns([3, 1])
                name_col.markdown(f"**{biz['name']}**")

                # Color the rating based on its value
                if biz["rating"] >= 4.5:
                    color = "#00c853"   # green
                elif biz["rating"] >= 4.0:
                    color = "#2196f3"   # blue
                else:
                    color = "#ff9800"   # orange

                rating_col.markdown(
                f"<p style='text-align:right; color:{color}; font-weight:bold;'>⭐ {biz['rating']}</p>",
                unsafe_allow_html=True
                )

                # Category tag and city in small text
                st.caption(f"📁 {biz['category']}  •  📍 {biz['city']}")

                # Description — truncated to 100 chars so cards stay the same height
                st.write(biz["desc"][:100] + ("…" if len(biz["desc"]) > 100 else ""))

                # "View details" button — unique key is REQUIRED when you have
                # multiple buttons. Without it, Streamlit can't tell them apart.
                if st.button("View details →", key=f"btn_{biz['id']}", use_container_width=True):
                    # Store which business was clicked in session_state.
                    # Session state persists across reruns — it's Streamlit's memory.
                    st.session_state["selected_biz"] = biz["id"]

    return results