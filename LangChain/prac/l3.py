import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Load the text file
from langchain_community.document_loaders import TextLoader

loader = TextLoader("a.txt")
data = loader.load()

# Split the text into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=500,
    chunk_overlap=50,
)

chunks = text_splitter.split_text(data[0].page_content)
print("Chunks:", chunks)

# Use Gemini Embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=api_key,
    model="models/embedding-001"  # ✅ Correct Gemini embedding model
)

# Store in FAISS
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

# Convert chunks to Document objects
docs = [Document(page_content=chunk) for chunk in chunks]

# Build the vectorstore
vectorstore = FAISS.from_documents(docs, embeddings)

# Query function
def query_store(query_text):
    results = vectorstore.similarity_search(query_text, k=3)
    return [doc.page_content for doc in results]

# Run a sample query
query_text = "the woman"
results = query_store(query_text)

# Print top 3 matching chunks
print("Top 3 Matching Chunks:")
for i, chunk in enumerate(results, 1):
    print(f"\nResult {i}:\n{chunk}")
