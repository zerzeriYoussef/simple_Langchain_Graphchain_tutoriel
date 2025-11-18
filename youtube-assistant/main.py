import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="youtube_form"):
        youtube_url = st.text_input("Enter YouTube URL")
        query = st.text_input("Enter your question")
        submit_button = st.form_submit_button("Submit")
if submit_button and query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response = lch.get_response_from_query(db, query)
    st.subheader("Answer")
    st.text(textwrap.fill(response, width=80))