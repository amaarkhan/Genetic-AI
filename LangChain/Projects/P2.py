'''
Project 2: Simulated Recipe Finder with Ingredient Matching 
Objective: Create a RAG-like system that helps users find recipes based on ingredients they have. This will simulate a more advanced search where the "query" might match only parts of the "documents." 
Concepts to Apply: 
Data Representation: Represent recipes as dictionaries or objects containing name, ingredients (list of strings), and instructions. Create a dataset of 5-10 mock recipes. 
Document Creation: For each recipe, create a "searchable document" string (e.g., combining recipe name and ingredients: "name: [Recipe Name], ingredients: [ingredient1], [ingredient2]..."). 
Simulated Embeddings: Generate mock embeddings for these searchable recipe documents. 
Vector Store: Store these recipe embeddings and their original recipe data (or a reference to it) in your SimpleVectorStore. 
Query Processing: When a user lists ingredients, create a query string from them (e.g., "recipes with: [user_ingredient1], [user_ingredient2]"). 
Retrieval: Use your retrieve_top_k to find recipes whose "searchable document" embeddings are most similar to the user's ingredient query embedding. 
Prompt Augmentation & Mock LLM: Augment a prompt to the mock LLM with the retrieved recipe details and ask it to "suggest a recipe you can make with these ingredients." 
Core Features: 
Define Mock Recipes: Create a Python list of dictionaries representing various recipes. 
Index Recipes: For each recipe, generate a searchable text representation, embed it, and add it to the SimpleVectorStore. 
User Ingredient Input: Prompt the user to enter a comma-separated list of ingredients they have. 
Generate Query Embedding: Create a mock embedding for the user's ingredient list. 
Retrieve Recipes: Find the top K most similar recipe documents from the vector store. 
Suggest Recipe: Augment the mock LLM's prompt with the retrieved recipe information (e.g., full recipe details or just names/key ingredients) and the user's query. Ask the mock LLM to suggest a recipe or list suitable recipes. 
Display Suggestion: Print the mock LLM's generated suggestion. 
Example Flow: 
--- Recipe Finder --- 
Enter ingredients you have (comma-separated, e.g., 'chicken, rice, broccoli'): [User Input] 
Searching for recipes... 
 
[Mock LLM Suggestion: "Based on your ingredients, you could make: 
Recipe Name: Chicken Stir-fry 
Ingredients: Chicken, Rice, Broccoli, Soy Sauce, Ginger 
Instructions: ... 
"] 
 
Want to find more recipes? (yes/no): 
> [User Input] 
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
    
    def print_all(self):
        for id, emb, text in self.lis:
            print(id, text, "\n")

        
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

# Sample Reciepies
recipies = {
    1 : {
        "name" : "Chicken Tikka",
        "ingredients": ["chicken", "masala", "seasoning"],
        "instructions": "Marinate the chicken and cook it"
    },
    2 : {
        "name" : "Burger",
        "ingredients": ["patty", "buns", "ketchup"],
        "instructions": "Cook the patty and assemble"
    },
    3 : {
        "name" : "car",
        "ingredients": ["dough", "chicken", "ketchup"],
        "instructions": "Cook the base and add chicken on top"
    },
    4 : {
        "name" : "pasta",
        "ingredients": ["pasta", "sauce", "vegetables"],
        "instructions": " Boil the pasta and add sauce with veggies"
    },
    5 : {
        "name" : "Pizza",
        "ingredients": ["dough", "chicken", "ketchup"],
        "instructions": "Cook the base and add chicken on top"
    },
    6 : {
        "name" : "Steak",
        "ingredients": ["beef", "butter", "vegetable"],
        "instructions": "Cook the steak in butter and then the veggies"
    },
    7 : {
        "name" : "Pulao",
        "ingredients": ["rice", "chicken", "beef", "seasoning"],
        "instructions": "Cook the rice with the chicken or beef"
    },
    8 : {
        "name" : "Plane",
        "ingredients": ["wings", "steering", "enginer"],
        "instructions": "Fly everything"
    },
}

def document_creator(dict):
    chunks = []
    for i in range (1,9):
        doc= ""
        print("right now item: ", dict[i].items(), "\n=============================")
        for x, obj in dict[i].items():
            # item = x + ": "
            item = ""
            
            if x=="ingredients":
                for y in obj:
                    # print(y)
                    item += y + " "
            else: 
                item += obj
            # print(item)
            doc += item
            doc+=" "
        chunks.append(doc)
        print(doc, "\n")
    return chunks


def run_rag_pipeline(query, vector_store, embedding_func, mock_llm_func, k=1):
    vector_store.print_all()
    emb=create_mock_embedding(query)
    nearest = vector_store.retrieve_top_k(emb, k)
    print("Nearest: ", nearest)
    prompt=augmented_prompt(query, nearest)
    print("Prompt: ", prompt)
    prompt=mock_llm_func(prompt, nearest[0])
    return prompt

vec = SimpleVectorStore(0, [], "")
chunks = document_creator(recipies)
index_doucment(chunks, vec, create_mock_embedding)

input_var=""
input_var = input("Enter the ingredients you have (comma-separated): ")

while input_var != "exit":
    final= run_rag_pipeline(input_var, vec, create_mock_embedding, mock_llm_response)
    print("Mock LLM Response: ", final)
    input_var = input("Enter the ingredients you have (comma-separated) or type 'exit' to quit: ")
    if input_var.lower() == "exit":
        break
    else:
        continue
    # print("Mock LLM Response: ", final)


