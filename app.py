import streamlit as st

st.title("madang DB")

conn = st.connection("neon", type="sql")

st.subheader("books")
book = conn.query("SELECT * FROM book ORDER BY bookid;", ttl=0)
st.dataframe(book)

st.subheader("customers")
customer = conn.query("SELECT * FROM customer ORDER BY custid;", ttl=0)
st.dataframe(customer)

st.subheader("orders")
orders = conn.query("SELECT * FROM orders ORDER BY orderid;", ttl=0)
st.dataframe(orders)
