import streamlit as st

def show_business_cards(businesses):
    cols = st.columns(3)

    for i, biz in enumerate(businesses):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="
                padding: 1rem;
                margin-bottom: 1rem;
                border-radius: 10px;
                background-color: #2a2a2a;
            ">
                <h4 style="color:white;">{biz['name']}</h4>
                <p style="color:#aaa;">
                    {biz['category']} • {biz['city']}
                </p>
                <p style="color:#ccc;">⭐ {biz['rating']}</p>
            </div>
            """, unsafe_allow_html=True)