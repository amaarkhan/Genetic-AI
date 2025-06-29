
'''
Section 3:Documents & Embeddings 
You are given a .txt file named a.txt containing a long article. Write a Python script using LangChain that: 

1. Loads the contents of data.txt. 
2. Split the text into chunks of 30 characters with 10-characters overlapping. 
3. Converts the chunks into embeddings using OpenAI embeddings model: text-embedding-3-small 
4. Stores the embeddings in a FAISS vector store. 
5. Implement a function to query the vector store and return the top 3 most similar chunks 
6. Store the below text in data.txt first and use it in your code: 
'''
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Load the text data
loader = TextLoader("a.txt")
documents = loader.load()
# Split the text into chunks
text_splitter = CharacterTextSplitter(
    separtor=["\n\n", "\n", " ", "."],
    chunk_size=30,
    chunk_overlap=10
)
chunks = text_splitter.split_documents(documents)
# Convert chunks into embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=api_key)
# Store embeddings in FAISS vector store
vector_store = FAISS.from_documents(chunks, embeddings)
# Function to query the vector store
def query_vector_store(query, top_k=3):
    query_embedding = embeddings.embed_query(query)
    results = vector_store.similarity_search_by_vector(query_embedding, k=top_k)
    return results

query= "Tell me about the main topic of the article."
results = query_vector_store(query)
for i, result in enumerate(results):
    print(f"Result {i+1}: {result.page_content}\n")



'''
Section 4: Tool usage 
Task: 

Create a LangChain agent that: 
1. Uses GPT-4o mini (gpt-4o-mini-2024-07-18) Vision to describe images 
2. Extracts object lists from descriptions 
3. Maintains proper tool execution order 

Requirements: 
Implement two tools: 

describe_image: Generates text descriptions using GPT-4o mini  
list_objects: Processes descriptions into bullet-point lists using GPT-4o mini 

Configure the agent to: 
Enforce tool execution sequence (description → extraction) 
'''

from langchain_community.tools import Tool
from langchain_community.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.llms import OpenAI
from langchain_community.prompts import ChatPromptTemplate
from langchain_community.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI                  
# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", openai_api_key=api_key)
# Define the describe_image tool
describe_image_tool = Tool(
    name="describe_image",
    func=lambda image: llm.invoke({"image": image, "prompt": "Describe this image in detail."}),
    description="Generates a detailed text description of the provided image."
)
# Define the list_objects tool
list_objects_tool = Tool(
    name="list_objects",
    func=lambda description: llm.invoke({"text": description, "prompt": "Extract a bullet-point list of objects from this description."}),
    description="Processes the text description and extracts a bullet-point list of objects."
)
# Create the agent with the tools
tools = [describe_image_tool, list_objects_tool]
agent = create_openai_tools_agent(
    llm=llm,
    tools=tools,
    prompt=ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that describes images and extracts object lists."),
        ("user", "Describe the image and then extract objects from the description.")
    ])
)
# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# Example usage
image_path = "p1.jpg"  # Replace with your image path
# Run the agent
result = agent_executor.run({"image": image_path})
print("Description:", result["describe_image"])
print("Object List:", result["list_objects"])

