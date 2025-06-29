import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")



from langchain_google_genai import ChatGoogleGenerativeAI

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Use valid Gemini model name
    google_api_key=api_key,
    temperature=0.5,
)

# Ask a question
response = llm.invoke("What is the capital of Pakistan?")
print("Response:", response)

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


prompt_template = PromptTemplate(
    input_variables=["question"],
    template="give me a short short story about {question}",
)
chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
)
# Run the chain with a question
output = chain.run(question=" peshawar")
print("Output:", output)

#import simplesequential chain
from langchain.chains import SimpleSequentialChain

# Chain 1: Get 3 job-related topics
summary_prompt = PromptTemplate.from_template(
    "List 3 technical topics someone applying as an {text} should be good at. Just list topics, no explanation."
)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

# Chain 2: Get interview questions from those topics
translation_prompt = PromptTemplate.from_template(
    "Give one interview question from each of these topics:\n\n{input}"
)
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

# Sequential chain
sequential_chain = SimpleSequentialChain(
    chains=[summary_chain, translation_chain],
    verbose=True,
)

# Run it
result = sequential_chain.run("AI agents engineer")
print("Interview Questions:\n", result)
