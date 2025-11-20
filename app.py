import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("retail.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("Retail Sales Dashboard")

# KPIs
st.subheader("Key Metrics")
total_revenue = df['Revenue'].sum()
avg_order_value = df['Revenue'].mean()
total_qty = df['Quantity'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Avg Order Value", f"${avg_order_value:,.2f}")
col3.metric("Total Quantity Sold", f"{total_qty:,}")

# Revenue Over Time
st.subheader("Revenue Over Time")
daily_rev = df.groupby('Date')['Revenue'].sum().reset_index()
fig1 = px.line(daily_rev, x='Date', y='Revenue')
st.plotly_chart(fig1)

# Category Sales
st.subheader("Revenue by Category")
cat_rev = df.groupby('Category')['Revenue'].sum().reset_index()
fig2 = px.bar(cat_rev, x='Category', y='Revenue')
st.plotly_chart(fig2)

# Top Products
st.subheader("Top 10 Products by Revenue")
top_products = (df.groupby('Product')['Revenue']
                .sum().sort_values(ascending=False)
                .head(10).reset_index())
fig3 = px.bar(top_products, x='Product', y='Revenue')
st.plotly_chart(fig3)

# Region Sales
st.subheader("Revenue by Region")
region_rev = df.groupby('Region')['Revenue'].sum().reset_index()
fig4 = px.bar(region_rev, x='Region', y='Revenue')
st.plotly_chart(fig4)

st.write("Dashboard created with Streamlit + Plotly")
