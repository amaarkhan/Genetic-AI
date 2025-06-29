'''
Section 1: Prompt Templates
Section 1.1
Create a LangChain script that uses ChatPromptTemplate to summarize text with the following requirements:
Use a system message to define the assistant's role: "You are a professional summarization assistant"
Use a human message template that takes {text} as input
Generate a 1-sentence summary that captures the key points
'''
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.5,
)

# Define the chat prompt
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a professional summarization assistant."),
    HumanMessagePromptTemplate.from_template("Summarize this text in one sentence: {text}"),
])

# Create the chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
)

# Input text to summarize
text = "LangChain is a framework for developing applications powered by language models. It provides modular components for building complex workflows.'" \
    "LangChain supports various tasks like question answering, summarization, and more. It integrates with multiple LLM providers and offers tools for data processing." 

# Run the chain
summary = chain.run(text=text)
print("Summary:", summary)


'''
Section 1.2
Task:
Using LangChain's FewShotPromptTemplate, create a simple sentiment classifier that:
Learns from examples like (1 positive, 1 negative)
Classifies new text inputs as either "Happy" or "Sad"
Formats the prompt clearly with examples and instructions
Requirements:
Define training examples. Like:
"text": "I got a promotion today!", "label": "Happy"
"text": "My dog passed away", "label": "Sad"
Test your classifier with:
"I failed my exam" (should return "Sad")

Question:
Write the complete Python code to implement this classifier using LangChain's few-shot learning components.
'''

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains import LLMChain

# Load .env and get API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Gemini LLM setup
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or gemini-2.5-flash if supported
    google_api_key=api_key,
    temperature=0.3
)

# Step 1: Few-shot examples
examples = [
    {"text": "I got a promotion today!", "label": "Happy"},
    {"text": "My dog passed away", "label": "Sad"},
]

# Step 2: Format for each example
example_prompt = PromptTemplate(
    input_variables=["text", "label"],
    template="Text: {text}\nSentiment: {label}\n"
)

# Step 3: Few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Classify the sentiment of the following text as either 'Happy' or 'Sad'.\n\n",
    suffix="Text: {text}\nSentiment:",
    input_variables=["text"]
)

# Step 4: LLM chain with Gemini
chain = LLMChain(
    llm=llm,
    prompt=few_shot_prompt
)

# Step 5: Run classification
text_input = "I failed my exam"
result = chain.run(text=text_input)

print("Sentiment:", result.strip())


'''
Section 2: Sequential chains
Section 2.1
Task:
Create a LangChain application that generates creative product names and slogans using sequential chains. Implement a system where:
The first step generates a company name based on a product description
The second step creates a slogan based on the generated company name
Both steps use Gemini

Requirements:
Define two prompt templates:
name_template: Takes {product} as input, outputs company name
Template: "Generate a creative name for a company that makes {product}"
slogan_template: Takes {company_name} as input, outputs slogan
Template: "Create a catchy slogan for this company: {company_name}"

Create two LLM chains:
name_chain with output key "company_name"
slogan_chain with output key "slogan"
Combine chains using SequentialChain and generate an output. Test with:
"eco-friendly water bottles"
(Example output: "AquaGreen Solutions" with slogan "Hydrate Sustainably!")
'''

name_template = PromptTemplate(
    input_variables=["product"],
    template="Generate one (No more than 1) creative name(simple) for a company that makes {product}"
)
slogan_template = PromptTemplate(
    input_variables=["company_name"],
    template="Create one(no more than 1) catchy slogan(simple) for this company: {company_name}"
)
from langchain.chains import LLMChain, SimpleSequentialChain
# Create LLM chains
name_chain = LLMChain(
    llm=llm,
    prompt=name_template,
    output_key="company_name"
)
slogan_chain = LLMChain(
    llm=llm,
    prompt=slogan_template,
    output_key="slogan"
)

main_chain = SimpleSequentialChain(
    chains=[name_chain, slogan_chain],
    verbose=True
)

ans= main_chain.run("eco-friendly water bottles")
print("Output:", ans)




'''
Section 2.2
You are building an AI assistant for job seekers. Create a SequentialChain that does the following:
Extracts the key responsibilities from a raw job description text.
Identifies the top 3 skills required for the job based on the extracted responsibilities.

Generates a personalized summary for a candidate, assuming their name is "Alex" and they are applying for the job.
Implement this 3-step pipeline using SequentialChain and multiple LLMChains in LangChain.
'''
extract_responsibilities_template = PromptTemplate(
    input_variables=["job_description"],
    template="Extract the key responsibilities from the following job description:\n\n{job_description}\n\nResponsibilities:"
)
identify_skills_template = PromptTemplate(
    input_variables=["responsibilities"],
    template="Based on these responsibilities, identify the top 3 skills required for the job:\n\n{responsibilities}\n\nSkills:"
)
generate_summary_template = PromptTemplate(
    input_variables=["skills"],
    template="Generate a personalized summary for a candidate named Alex applying for this job with the following skills:\n\n{skills}\n\nSummary:"
)
from langchain.chains import LLMChain, SequentialChain
# Create LLM chains
extract_chain = LLMChain(
    llm=llm,
    prompt=extract_responsibilities_template,
    output_key="responsibilities"
)
identify_skills_chain = LLMChain(
    llm=llm,
    prompt=identify_skills_template,
    output_key="skills"
)
generate_summary_chain = LLMChain(
    llm=llm,
    prompt=generate_summary_template,
    output_key="summary"
)
# Combine chains into a sequential chain
job_chain = SequentialChain(
    chains=[extract_chain, identify_skills_chain, generate_summary_chain],
    input_variables=["job_description"],
    output_variables=[ "summary"],
    verbose=True
)
# Example job description
job_description = "A Front-End Developer is responsible for building the visual and interactive elements of websites and web applications, ensuring a seamless user experience and optimizing for performance, responsiveness, and cross-browser compatibility. Their role involves translating UI/UX designs into functional code using languages like HTML, CSS, and JavaScript, and often utilizing frameworks such as React, Vue, or Angular."

# Run the chain
summary = job_chain.run(job_description=job_description)
#print responsibilities, skills, and summary

print("Personalized Summary for Alex:\n", summary)
