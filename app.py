import streamlit as st

with st.sidebar: 
    st.set_page_config(page_title="RAG Question Answer ")
    st.header(" RAG Question Answer")
    uploaded_file = st.file_uploader(
        "** Upload PDF files for AnA**", type=["pdf"], accept_multiple_files=False
    )
    
    process = st.button(
        "Process",
    )
