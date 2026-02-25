st.markdown("""
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background: #f5f7fa;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background: #eef2f7;
}

/* Remove the default white block behind content */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Nice header card */
.header-banner {
    background: #003366;
    padding: 18px 20px;
    border-radius: 10px;
    margin: 0 0 16px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.header-banner h1 {
    color: white;
    margin: 0;
    font-size: 28px;
    line-height: 1.1;
}
.header-banner p {
    color: rgba(255,255,255,0.85);
    margin: 6px 0 0 0;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-banner">
  <h1>ALPA - Higher Logic Analytics</h1>
  <p>Email engagement dashboard (opens, clicks, trends)</p>
</div>
""", unsafe_allow_html=True)
