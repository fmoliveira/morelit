import streamlit as st
import notmuch2

db = notmuch2.Database()
filter = "unread tag:inbox"

st.write("# morelit")
st.write("unread messages:", db.count_messages(filter))
