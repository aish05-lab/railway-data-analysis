import streamlit as st
import pandas as pd

st.set_page_config(page_title="Railway Data Analysis", layout="wide")
st.title("🚆 Railway Data Analysis")
st.write("Passenger statistics and train delay analysis")

df = pd.read_csv("data/railway.csv")
df.columns = df.columns.str.strip()

df["Delay_Min"] = pd.to_numeric(df["Delay_Min"], errors="coerce")
df["Passengers"] = pd.to_numeric(df["Passengers"], errors="coerce")

c1, c2, c3 = st.columns(3)
c1.metric("Total trains", len(df))
c2.metric("Total passengers", f"{df['Passengers'].sum():,.0f}")
c3.metric("Average delay", f"{df['Delay_Min'].mean():.2f} min")

st.subheader("Top 5 most delayed trains")
top = df.nlargest(5, "Delay_Min")[["Train_Name", "Delay_Min"]]
st.bar_chart(top.set_index("Train_Name"))

st.subheader("Railway dataset")
st.dataframe(df, use_container_width=True)
