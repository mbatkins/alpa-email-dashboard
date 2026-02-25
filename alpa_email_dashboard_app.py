import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="ALPA - Higher Logic Analytics",
    layout="wide"
)

# Title
st.title("ALPA - Higher Logic Analytics")
st.markdown("Email engagement dashboard (opens, clicks, trends)")

@st.cache_data
def load_data():
    df = pd.read_csv("ALPA_Email_Analytics_Cleaned.csv")
    df["last_sent"] = pd.to_datetime(df["last_sent"], errors="coerce")
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter by Airline Group")
groups = sorted(df["group_name"].dropna().unique())
selected_group = st.sidebar.selectbox("Select Airline Group", groups)

filtered = df[df["group_name"] == selected_group].sort_values("last_sent", ascending=False)

# Layout columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"{selected_group} - Recent Campaign Open Rates")
    st.bar_chart(
        filtered.set_index("message")["opened%"].head(20)
    )

with col2:
    st.subheader("Quick Stats")
    st.metric("Avg Open Rate", f"{filtered['opened%'].mean():.2f}%")
    st.metric("Avg Click Rate", f"{filtered['clicked%'].mean():.2f}%")

st.subheader("Campaign Details")
st.dataframe(
    filtered[[
        "last_sent",
        "message",
        "sent",
        "delivered%",
        "opened%",
        "clicked%",
        "bounced%",
        "opt_out%"
    ]]
)
