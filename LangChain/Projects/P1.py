'''
Project 1: Local Document Q&A Chatbot 

Objective: Develop a simple RAG-based Q&A chatbot that can answer questions based on the content of a local text file 
(e.g., a .txt file containing a fictional story, a Wikipedia article, or a policy document). 

Concepts to Apply: 
Document Loading: Read content from a local .txt file. 
Text Splitting/Chunking: Divide the document into smaller, manageable chunks. 
Simulated Embeddings: Use your create_mock_embedding function from Section 1 to generate embeddings for each chunk. 
Vector Store: Use your SimpleVectorStore class to store the chunks and their embeddings. 
Retrieval: Implement the retrieve_top_k method to find relevant chunks based on a user query. 
Prompt Augmentation: Construct an augmented prompt that combines the user's query and the retrieved context. 
Mock LLM: Use your mock_llm_response function to simulate the LLM's answer generation. 
Basic Chat Loop: Implement a simple command-line interface where the user can enter questions, and the chatbot provides answers. 

Core Features: 
Load Document: User specifies a .txt file to load. 
Index Document: The system reads the file, chunks it, generates mock embeddings, and stores them in the vector store. 
User Query Input: Prompt the user to enter a question. 
Retrieve Context: Convert the user's question into a mock embedding, then retrieve the top K relevant chunks from the vector store. 
Generate Response: Augment a prompt with the retrieved context and the user's query, then feed it to the mock LLM. 
Display Answer: Print the mock LLM's response. 
Loop: Allow continuous questioning until the user types 'exit'. 

Example Flow: 
--- Local Document Q&A Chatbot --- 
Enter path to text document (e.g., 'my_story.txt'): [User Input] 
 
Indexing document... Done. 
 
Ask me a question (type 'exit' to quit): 
> [User Question] 
Thinking... 
[Mock LLM Answer based on retrieved context] 
 
Ask me another question (type 'exit' to quit): 
> [User Question] 
... 
'''
import numpy as np



def magnitude(vec):
    sum = 0
    for i in range(len(vec)):
        sum += vec[i] ** 2
    return np.sqrt(sum)


def dot(vec1, vec2):
    return sum(vec1[i] * vec2[i] for i in range(min(len(vec1), len(vec2))))

def cosine_similarity(vec1, vec2):
    a = dot(vec1, vec2)
    b = magnitude(vec1)
    c = magnitude(vec2)
    if b == 0 or c == 0:
        return -1
    return a / (b * c)


def load_and_split_text(long_text, chunk_size=50):
    chunks = []
    if chunk_size <= 0:
        print("Chunk size must be positive.")
        return chunks

    while long_text.strip():
        if len(long_text) <= chunk_size:
            chunks.append(long_text.strip())
            break

        if long_text[chunk_size] == " ":
            chunks.append(long_text[:chunk_size].strip())
            long_text = long_text[chunk_size:].strip()
        else:
            i = chunk_size
            while i < len(long_text) and long_text[i] != " ":
                i += 1
            if i >= len(long_text):
                chunks.append(long_text.strip())
                break
            chunks.append(long_text[:i].strip())
            long_text = long_text[i:].strip()
    return chunks


def create_mock_embedding(text):
    embedding = []
    for i in range(len(text)):
        x1= 1 + ord(text[i])
        x2= 1 / x1
        x = 1 - x2
        embedding.append(x)
    return embedding

    

class SimpleVectorStore:
    def __init__ (self,doucment_id,embedding,original_text):
        tup = tuple((doucment_id,embedding, original_text))
        self.lis = list()
        self.lis.append(tup)

    def add_doucment(self, doucment_id, embedding, text):
        tup = tuple((doucment_id, embedding, text))
        self.lis.append(tup)
        # print(self.lis)    

    def get_all_embeddings(self):
        embeds = []
        for id, emb, text in self.lis:
            embeds.append(emb)
        return embeds

    def get_doucment_by_id(self, doucment_id):
        for id,emb,text in self.lis:
            if id == doucment_id:
                return text
        return "none"

    def retrieve_top_k(self, query_embedding, k=3):
        vals=[]
        for id,emb,text in self.lis:
            sim = cosine_similarity(emb, query_embedding)
            vals.append((id, text, sim))
        vals.sort(key=lambda x: x[2], reverse=True)
        final_vals = []
        for node in vals:
            if k == 0:
                break
            else:    
                final_vals.append(node)
                k -= 1
        return final_vals   

        
def index_doucment(text,vector_store_instance,embedding_function):
    index=1
    for i in text:
        embedding = embedding_function(i)
        vector_store_instance.add_doucment(index, embedding, i)
        index += 1


def augmented_prompt(query,retrieved_texts):
    prompt = f"you are a assistant that helps in retriving documents based on similairty. Find {query} in {retrieved_texts}"
    return prompt

def mock_llm_response(prompt, nearest) :
    return f"Based on the provided information, I can answer your question. I am thrilled to announce that your query..... matches with {nearest[0]}"

f=open ("a.txt")
data= f.read()
print("Document Loaded Successfully")
print(data)

chunks = load_and_split_text(data, chunk_size=50)
print("Document Split into Chunks Successfully")

vector_store = SimpleVectorStore(1, create_mock_embedding(chunks[0]), chunks[0])
index_doucment(chunks, vector_store, create_mock_embedding)
print("Document Indexed Successfully")

while True:
    query = input("Ask me a question (type 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    query_embedding = create_mock_embedding(query)
    nearest = vector_store.retrieve_top_k(query_embedding, k=3)

    if not nearest:
        print("No relevant documents found.")
        continue

    retrieved_texts = [text for _, text, _ in nearest]
    augmented = augmented_prompt(query, retrieved_texts)
    
    response = mock_llm_response(augmented, nearest)
    print(response)
    print("Thinking...")
    print("Answer:", response)
# Close the file after reading
f.close()
# End of the code