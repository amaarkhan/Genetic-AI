
'''
Cosine Similarity measures the cosine of the angle between two vectors. If two vectors are pointing in the same direction, the angle between them is zero, and the cosine is 1



Question 1.1: Write a Python function create_mock_embedding(text) that takes a string and returns a simple list of 3 floating-point numbers as its "embedding." Make the numbers slightly different for different inputs (e.g., based on len(text) or character sums) to simulate unique embeddings. 
'''
def create_mock_embedding(text):

    embedding =[]
    for i in text:
        x1=1+ord(i)
        x2=1/x1
        x=1-x2
        embedding.append(x)
    return embedding[:3]  


print(create_mock_embedding("Amaar")) 



'''
Question 1.2: Use your create_mock_embedding function to generate embeddings for three short sentences: "The cat sat on the mat.", "The dog barked loudly.", and "A small feline rested on a rug." Store these sentences along with their mock embeddings in a list of tuples (sentence, embedding). 
'''
sentences = [
    "The cat sat on the mat.",
    "The dog barked loudly.",
    "A small feline rested on a rug."
]
embeddings = [(sentence, create_mock_embedding(sentence)) for sentence in sentences]
print(embeddings)



'''
Question 1.3: Modify create_mock_embedding to ensure that if the input text is identical, the exact same mock embedding is returned. 
This simulates deterministic embedding models. 
'''

from sklearn.metrics.pairwise import cosine_similarity

a=create_mock_embedding("i am amaar")
b=create_mock_embedding ("i am amaar")

print("Embedding for 'i am amaar':", a)
print("Embedding for 'i am amaar':", b)

if a==b:
    print("The embeddings are the same")