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
orders = conn.query("""
    SELECT o.orderid, c.name AS 고객명, b.bookname AS 책이름,
           o.saleprice AS 판매가, o.orderdate AS 주문일
    FROM orders o
    JOIN customer c ON o.custid = c.custid
    JOIN book b ON o.bookid = b.bookid
    ORDER BY o.orderid;
""", ttl=0)
st.dataframe(orders)
