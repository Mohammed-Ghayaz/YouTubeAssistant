from langchain_community.document_loaders import YoutubeLoader
from trial import get_subtitle_url, get_subtitles
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document

load_dotenv()


def create_vectordb(url: str) -> FAISS:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    subtitle_url = get_subtitle_url(url)
    transcript = get_subtitles(subtitle_url)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(transcript)
    docs = [Document(page_content=chunk, metadata={"source": url}) for chunk in chunks]

    db = FAISS.from_documents(docs, embeddings)

    return db

def get_response_from_query(query, db, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = GoogleGenerativeAI(model="gemini-2.5-flash")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
            Imagine you are a very useful YouTube assistant, who could answer questions about videos based on the transcript.

            Your task is to answer the question: {question}
            with the help of the following video transcript: {docs}

            Only use the factual information from the video transcripts. If you feel like you don't
            have enough information for the question from the transcript, just return "I don't know" as a response.
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": query,
        "docs": docs_page_content
    })

    return response




