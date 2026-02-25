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

filtered = df[df["group_name"] == selected_group].copy()

# Sort newest first for table, but we’ll build the chart separately
filtered = filtered.sort_values("last_sent", ascending=False)

# Layout columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"{selected_group} - Campaign Open Rates (Chronological)")

    # Take the most recent 20 campaigns, then re-sort oldest -> newest for the bar chart
    recent20 = filtered.dropna(subset=["last_sent"]).head(20).copy()
    recent20 = recent20.sort_values("last_sent", ascending=True)

    # Build a label that includes date so duplicate subject lines are still readable
    recent20["label"] = recent20["last_sent"].dt.strftime("%m/%d") + " — " + recent20["message"].astype(str)

    st.bar_chart(
        recent20.set_index("label")["opened%"]
    )

with col2:
    st.subheader("Quick Stats")
    st.metric("Avg Open Rate", f"{filtered['opened%'].mean():.2f}%")
    st.metric("Avg Click Rate", f"{filtered['clicked%'].mean():.2f}%")

st.subheader("Campaign Details (Newest First)")
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
