'''
Question 1.4: Define a Python class SimpleVectorStore. Its __init__ method should initialize an empty list to store (document_id, embedding,
 original_text) tuples. Add a method add_document(document_id, text, embedding).
'''

class SimpleVectorStore:
    def __init__ (self,doucment_id, text, embedding):
        tup=tuple(document_id, text, embedding)
        self.lis=list()
        self.lis.append(tup)

    def add_document(self, document_id, text, embedding):
        tup = (document_id, text, embedding)
        self.lis.append(tup)

    def get_all_embeddings(self):
        embeds =[]
        for id, emb, text in self.lis:
            embeds.append(emb)
        
        return embeds
    
    def get_document_by_id(self, document_id):
        for id, emb, text in self.lis:
            if id == document_id:
                return text 
            

'''
Question 1.5: Populate your SimpleVectorStore with 5 example short texts (e.g., facts about animals, historical dates) and their mock embeddings generated using your function from Q1.1.
'''
def create_mock_embedding(text):

    embedding =[]
    for i in text:
        x1=1+ord(i)
        x2=1/x1
        x=1-x2
        embedding.append(x)
    return embedding[:3] 

emb1 = create_mock_embedding("The cat sat on the mat.")

s1 = SimpleVectorStore(1, emb1, "The cat sat on the mat." )

emb2 = create_mock_embedding("The dog barked loudly.")
emb3 = create_mock_embedding("A small feline rested on a rug.")
emb4 = create_mock_embedding("Pakistan was founded in 1947.")
emb5 = create_mock_embedding("Amaar was born in 2004")

s1.add_document(2, emb2,"The dog barked loudly.")
s1.add_document(3, emb3,"A small feline rested on a rug.")
s1.add_document(4, emb4,"Pakistan was founded in 1947.")
s1.add_document(5, emb5,"Amaar was born in 2004")

'''
Question 1.6: Add a method get_all_embeddings() to your SimpleVectorStore class that returns a list of just the embeddings stored, and another method get_document_by_id(document_id) that returns the original_text for a given ID.
'''

print(s1.get_all_embeddings(), "\n")
print("Id of this is:", s1.get_document_by_id(4))


'''
Question 1.7: Write a Python function calculate_dot_product(vec1, vec2) that takes two lists of numbers (representing vectors) and returns their dot product. 
'''

def calculate_dot_product(vec1, vec2):
    sum =0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum

print("Dot product is:", calculate_dot_product([1,2,3],[4,5,6]))

'''
Question 1.8: Write a Python function calculate_magnitude(vec) that takes a list of numbers and returns its magnitude (Euclidean norm). 
'''
import math
def calculate_magnitude(vec):
    res = 0
    for v in vec:
        res+= v**2

    return math.sqrt(res)

print("Magnitutuede is:", calculate_magnitude([3,4]))

'''
Question 1.9: Using calculate_dot_product and calculate_magnitude, implement calculate_cosine_similarity(vec1, vec2) which returns the cosine similarity between two vectors. (Formula: (vec1 . vec2) / (||vec1|| * ||vec2||)). Handle division by zero if a magnitude is zero. 
'''
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(vec1, vec2):
    '''
    Formula ye hai: (vec1 . vec2) / (||vec1|| * ||vec2||)
    '''
    num = calculate_dot_product(vec1, vec2)
    div = calculate_magnitude(vec1) * calculate_magnitude(vec2)

    if div == 0:
        return -1
    else:
        return (num/div)
        




        