import streamlit as st

def show_hero():
    st.markdown("""
    <div style="
      background: linear-gradient(135deg, #1a1e2b, #2d1f3d);
      padding: 3rem 2rem;
      border-radius: 12px;
      text-align: center;
      margin-bottom: 1.5rem;
    ">
      <h1 style="color: white; font-size: 2.4rem; margin-bottom: 0.5rem;">
        🏪 Business Directory
      </h1>
      <p style="color: rgba(255,255,255,0.6); font-size: 1.1rem;">
        Discover local businesses in your area
      </p>
    </div>
    """, unsafe_allow_html=True)