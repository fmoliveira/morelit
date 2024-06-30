import streamlit as st
import pandas as pd
import notmuch2

from datetime import datetime

db = notmuch2.Database()
filter = "unread tag:inbox"

st.set_page_config(layout="wide")
st.write("# morelit")
st.write("unread messages:", db.count_messages(filter))

headers = ["date", "from", "subject"]
list = []

for index, msg in zip(range(100), db.messages(filter, sort=db.SORT.NEWEST_FIRST)):
  list.append([
    datetime.fromtimestamp(msg.date),
    msg.header("from"),
    msg.header("subject"),
  ])

df = pd.DataFrame(list, columns=headers)
st.write(df)
