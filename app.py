import streamlit as st

st.title("마당서점 DB")

conn = st.connection("neon", type="sql")

st.subheader("도서 목록")
book = conn.query("SELECT * FROM book ORDER BY bookid;", ttl=0)
st.dataframe(book)

st.subheader("고객 목록")
customer = conn.query("SELECT * FROM customer ORDER BY custid;", ttl=0)
st.dataframe(customer)

st.subheader("주문 내역 (고객명 + 책 이름)")
orders = conn.query("""
    SELECT o.orderid, c.name AS 고객명, b.bookname AS 책이름,
           o.saleprice AS 판매가, o.orderdate AS 주문일
    FROM orders o
    JOIN customer c ON o.custid = c.custid
    JOIN book b ON o.bookid = b.bookid
    ORDER BY o.orderid;
""", ttl=0)
st.dataframe(orders)