from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def create_vector_db_from_youtube_url(youtube_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(youtube_url)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore


def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = "\n".join([doc.page_content for doc in docs])

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful assistant that can answer questions about YouTube video transcripts.

Answer the following question based on the transcript only.

Question:
{question}

Transcript:
{context}

If the question is not related to the transcript, say "I don't know".
Your answer should be detailed and concise.
        """
    )

    chain = prompt | llm
    response = chain.run({"question": query, "context": docs_page_content})
    return response


# Test run
if __name__ == "__main__":
    db = create_vector_db_from_youtube_url(youtube_url)
    print(get_response_from_query(db, "What is this video about?"))
