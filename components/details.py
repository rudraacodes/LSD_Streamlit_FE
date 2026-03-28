import streamlit as st
from utils.data_loader import load_businesses
BUSINESSES = load_businesses()
def show_details():
    selected_id = st.session_state.get("selected_biz")

    if selected_id:
        # Find the matching business from the full list (not just `results`,
        # because the user might filter the list after clicking)
        match = next((b for b in BUSINESSES if b["id"] == selected_id), None)

        if match:
            st.divider()

            # st.expander() collapses content behind a click-to-expand header.
            # expanded=True means it opens automatically when a card is clicked.
            with st.expander(f"📋 {match['name']} — Full Details", expanded=True):

                # Two-column layout: details on the left, a fake review on the right
                left, right = st.columns([2, 1])

                with left:
                    st.markdown(f"### {match['name']}")
                    st.caption(f"Category: **{match['category']}**  |  City: **{match['city']}**")
                    st.write(match["desc"])

                    # st.metric shows a big number with an optional delta (change indicator)
                    st.metric("Rating", f"⭐ {match['rating']} / 5.0")

                with right:
                    st.markdown("**Leave a review**")

                    # A form groups widgets together — nothing submits until the button
                    # is clicked. Without a form, every keystroke in the text area
                    # triggers a full rerun, which would be janky.
                    with st.form(f"review_{match['id']}"):
                        stars = st.select_slider(
                        "Your rating",
                        options=[1, 2, 3, 4, 5],
                        format_func=lambda x: "⭐" * x
                        )
                        review_text = st.text_area("Your thoughts", height=80)
                        submitted = st.form_submit_button("Submit review")

                        if submitted:
                            if review_text.strip():
                                st.success(f"Thanks for your {stars}⭐ review!")
                                # In a real app you'd send this to your FastAPI here:
                                # api_client.post_review(match["id"], stars, review_text)
                            else:
                                st.warning("Please write something before submitting.")

                # Close button — clears the session key and reruns so the panel hides
                if st.button("✕ Close", key="close_detail"):
                    del st.session_state["selected_biz"]
                    st.rerun()