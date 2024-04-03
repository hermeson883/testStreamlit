import streamlit as st

col1, col2, col3 = st.columns(3)

col1.write("Teste de boas vindas")
col1.map()

col2.image("https://images.unsplash.com/photo-1581351123004-757df051db8e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGdhbWVzfGVufDB8fDB8fHww")

col3.video("https://www.youtube.com/watch?v=s3sCmdBpusQ&t=185s&ab_channel=ANCAPSU")


st.map()