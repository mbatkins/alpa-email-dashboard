
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ALPA Email Analytics", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("ALPA_Email_Analytics_Cleaned.csv")
    df["last_sent"] = pd.to_datetime(df["last_sent"], errors="coerce")
    return df

df = load_data()

st.title("ALPA Email Performance Dashboard")

# Sidebar group selector
groups = sorted(df["group_name"].dropna().unique())
selected_group = st.sidebar.selectbox("Select Airline Group", groups)

filtered = df[df["group_name"] == selected_group].sort_values("last_sent", ascending=False)

st.subheader(f"{selected_group} - Recent Campaign Open Rates")

st.bar_chart(
    filtered.set_index("message")["opened%"].head(25)
)

st.subheader("Campaign Table")

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
