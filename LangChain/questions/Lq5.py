import math
def dot_product(vec1, vec2):
    sum = 0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum

def magnitude(vec):
    res = 0
    for v in vec:
        res += v ** 2
    return math.sqrt(res)

def cosine_similarity(vec1, vec2):
    num = dot_product(vec1, vec2)
    div = magnitude(vec1) * magnitude(vec2)

    if div == 0:
        return -1
    else:
        return (num / div)
    

#Document Loading and Chunking (Simple) 
# Question 2.1: Write a Python function load_and_split_text(long_text, chunk_size=50). 
# This function should take a long string and split it into chunks of approximately chunk_size characters,
#  ensuring chunks don't cut words in half (simple approach: split by space and combine words until chunk_size is met or exceeded).
#  Return a list of these text chunks

def load_and_split_text(long_text,chunk_size=50):
    words = long_text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_size:  # +1 for space
            if current_chunk:
                current_chunk += " "
            current_chunk += word
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


print(load_and_split_text("This is a long text that needs to be split into smaller chunks without cutting words in half. The function should ensure that each chunk is approximately of the specified size."))


'''
Question 2.2: Take a sample paragraph (e.g., 200-300 words) about a general topic (like "The history of computers").
 Use load_and_split_text to split it into chunks of chunk_size=100.
   Print each chunk and its length. Indexing Data 
'''

sample_text = ("This is a sample paragraph about the history of computers. Computers have evolved significantly over the decades, starting from the early mechanical devices to today's powerful machines. The first electronic computers were developed in the mid-20th century, and they were large, expensive, and used primarily for scientific calculations. As technology advanced, computers became smaller, more affordable, and accessible to the general public. The introduction of personal computers in the 1970s revolutionized the industry, allowing individuals to own and use computers at home and work. Today, computers are an integral part of our daily lives, used for everything from communication to entertainment to complex data analysis."
)
print (len(sample_text))

chunks = load_and_split_text(sample_text, chunk_size=100)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} (Length: {len(chunk)}): {chunk}\n")


'''
Question 2.3: Create a function index_documents(texts, vector_store_instance, embedding_function) that takes a list of text chunks, 
your SimpleVectorStore instance, and your create_mock_embedding function. It should iterate through the texts, generate an embedding for each using
 embedding_function, and add them to the vector_store_instance with a unique ID for each chunk
'''
def create_mock_embedding(text): #From Q1.1
    embedding = []

    for char in text:   
        x1 = 1 + ord(char)
        x2 = 1 / x1
        x = 1 - x2
        embedding.append(x)
    return embedding


class SimpleVectorStore:
    def __init__(self, document_id, embedding, original_text):
        tup = tuple((document_id,embedding, original_text))
        self.lis = list()
        self.lis.append(tup)

    def add_document(self, document_id,embedding ,text ):
        tup = tuple(( document_id,  embedding, text))
        self.lis.append(tup)
        # print(self.lis)

    def get_all_embeddings(self):
        embeds =[]
        for id, emb, text in self.lis:
            embeds.append(emb)
        
        return embeds
    
    def get_document_by_id(self, document_id):
        for id, emb, text in self.lis:
            if id == document_id:
                return text
        return "none"    
    
'''
    Retrieval Step 
    Question 2.6: Add a method retrieve_top_k(query_embedding, k=1) to your SimpleVectorStore class. This method should: 
    Calculate the cosine similarity between query_embedding and every embedding stored in the vector store. 
    Return the k (default 1) (document_id, original_text, similarity_score) tuples with the highest similarity scores, sorted in descending order of similarity. 
'''
def retrieve_top_k(self, query_embedding, k=1):
        vals = []
        for id, emb, text in self.lis:
            sim = cosine_similarity(emb, query_embedding)
            vals.append((id, text, sim))
        
        vals.sort(key=lambda x: x[2], reverse=True)

        final_vals = []

        for node in vals:
            if k==0:
                break
            else:    
                final_vals.append(node)
                k-=1
        return final_vals    



def index_documents(texts, vector_store_instance, embedding_function):
    for i, text in enumerate(texts):
        embedding = embedding_function(text)
        vector_store_instance.add_document(i + 1, embedding, text)


'''
Question 2.4: Take your 200-300 word sample paragraph from Q2.2, split it, and then use index_documents to add all its chunks
 and their mock embeddings to a new instance of your SimpleVectorStore.
'''
vector_store = SimpleVectorStore(0, [], "")
index_documents(chunks, vector_store, create_mock_embedding)
print("All embeddings in the vector store:")
print(vector_store.get_all_embeddings())



'''
. Question 2.5: After indexing, verify that your chunks are stored by iterating through the vector_store_instance's internal storage 
and printing a few document IDs and their corresponding original texts. Retrieval Step 
'''
for i in range(1, 6):
    print(f"Document ID {i}: {vector_store.get_document_by_id(i)}")


'''
Question 2.7: Formulate a sample "query" string related to your indexed paragraph (e.g., "When was the first computer invented?").
 Generate a mock embedding for this query. Then, use retrieve_top_k on your SimpleVectorStore to find the top 2 most relevant chunks. 
 print the retrieved chunks and their similarity scores. Augmenting the Prompt & Full RAG Chain (Conceptual/Mock LLM) Question
'''
s1 = SimpleVectorStore(0, [0,0,0], "")
query = "When was the first computer invented?"
query_embedding = create_mock_embedding(query)
top_k_results = retrieve_top_k(s1, query_embedding, k=2)
print("Top K Results:")
'''
2.8: Write a Python function augment_prompt(query, retrieved_texts) that takes a user query string and a list of retrieved_texts
 (the actual text content of the chunks). It should return a single string representing the augmented prompt,
   clearly indicating the context from the retrieved texts and the original query
'''
def augment_prompt(query, retrieved_texts):
    context = "\n".join(retrieved_texts)
    return f"Context:\n{context}\n\nQuery: {query}"
augmented_prompt = augment_prompt("When was the first computer invented?", [text for _, text, _ in top_k_results])
print("Augmented Prompt:")
print(augmented_prompt)


# Question 2.9: Simulate a simple LLM response. Write a function mock_llm_response(prompt) that takes the augmented prompt string and 
# returns a hardcoded, generic response (e.g., "Based on the provided information, I can answer your question."). 
# This is a placeholder for an actual LLM call. 

def mock_llm_response(prompt):
    return "Based on the provided information, I can answer your question."
response = mock_llm_response(augmented_prompt)
print("Mock LLM Response:")
