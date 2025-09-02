# YouTube Subtitle RAG with FAISS and LangChain

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline using **YouTube subtitles**, **FAISS vector database**, and **LangChain** with **Google Generative AI embeddings**.

The system:
1. Downloads YouTube subtitles (auto-generated or uploaded).
2. Splits the transcript into chunks.
3. Embeds the chunks into a **FAISS vector store**.
4. Uses LangChain to answer questions about the video content.

---

## 🚀 Features
- Extract subtitles from YouTube videos.
- Generate embeddings using **Google Gemini embedding model**.
- Store and query subtitle chunks in **FAISS**.
- Ask natural language questions about the video.
- Integration with **LangChain Runnables** pipeline.

---

## 📂 Project Structure

youtube-subtitle-rag/

├── main.py # Entry point to run the app

├── trial.py # Subtitle extraction utilities

├── langchain_helper.py # VectorDB creation using FAISS

├── README.md # Project documentation

## 📦 Dependencies

- **yt_dlp** – Download YouTube subtitles and metadata  
- **langchain** – Orchestration framework  
- **faiss-cpu** – Vector database for embeddings  
- **google-generativeai** – Google Gemini embeddings + LLMs

## 📝 Notes

- Some videos may not have subtitles → check available languages with `yt_dlp`.  
- Auto-generated subtitles may contain errors.  
- Ensure your Google API key is set as an environment variable: 

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

## 📖 Example Query

**Input:**

```text
What are the main topics discussed in the video?
```

**Output:**

```text
The video mainly discusses RAG pipelines, embeddings, and how to use LangChain with FAISS for Q&A systems.
```

## 🚀 Future Improvements

- Add support for multiple subtitle languages  
- Support for local video/audio transcripts

---

## 📜 License

MIT License © 2025 Z Mohammed Ghayaz

---

## 👤 Author

**Z Mohammed Ghayaz**  
- GitHub: [@Mohammed-Ghayaz](https://github.com/Mohammed-Ghayaz)  
- LinkedIn: [Mohammed Ghayaz](https://www.linkedin.com/in/mohammed-ghayaz/)  
- Email: mdghayaz04@gmail.com 

