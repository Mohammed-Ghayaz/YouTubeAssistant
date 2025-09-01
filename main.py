import streamlit as st
from langchain_helper import create_vectordb, get_response_from_query
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


st.set_page_config(
	page_title="YouTube Assistant",
	page_icon="📺",
	layout="centered",
	initial_sidebar_state="expanded"
)

st.markdown(
	"""
	<style>
	.main-title {
		font-size: 2.5em;
		font-weight: bold;
		color: #FF0000;
		text-align: center;
		margin-bottom: 0.5em;
	}
	.subtitle {
		font-size: 1.2em;
		color: #333;
		text-align: center;
		margin-bottom: 2em;
	}
	.stButton>button {
		background-color: #FF0000;
		color: white;
		font-size: 1em;
		border-radius: 8px;
		padding: 0.5em 2em;
	}
	</style>
	""",
	unsafe_allow_html=True
)

st.markdown('<div class="main-title">YouTube Assistant 📺</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Summarize, search, and interact with YouTube videos using AI!</div>', unsafe_allow_html=True)

with st.form("youtube_form"):
	youtube_url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")
	query = st.text_area("Ask a question about the video:", placeholder="e.g. What is the main topic?")
	submitted = st.form_submit_button("Get Response")

if submitted:
	with st.spinner("Processing video and generating response..."):
		try:
			vectordb = create_vectordb(youtube_url)
			response = get_response_from_query(query, vectordb)
			st.success("Response generated!")
			st.markdown(f"<div style='background-color:#f9f9f9; border-radius:10px; padding:20px;'><b>Answer:</b><br>{response}</div>", unsafe_allow_html=True)
		except Exception as e:
			st.error(f"Error: {e}")