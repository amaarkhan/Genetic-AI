import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Use valid Gemini model name
    google_api_key=api_key,
    temperature=0.5,
)

my_examples = [
    {
        "text": "The product is terrible",
        "sentiment" : "Negative"
    },
    {
        "text": "Super helpful, worth it",
        "sentiment": "Positive"
    }
]

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt_template = PromptTemplate(
    input_variables=["text"],
    template="What is the sentiment of this text: {text}",
)
chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
)
# Run the chain with a text
output = chain.run(text="the package is not opened yet")
print("Output:", output)


from langchain.agents import Tool
from langchain.agents import  AgentType, initialize_agent
from langchain_community.agent_toolkits import load_tools



# Define a simple multiply tool
def multiply(a: int, b: int = 1) -> int:
    return a * b

# Wrap the tool so the agent can parse input like "2025, 2"
mult_tool = Tool(
    name="multiply",
    func=lambda x: multiply(*map(int, x.split(","))),
    description="Multiplies two integers. Input should be in the format: 'a,b'"
)

# Only using our custom tool
tools = [mult_tool]

# Create the agent with Gemini and the multiply tool
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
print(agent.run("What is the age of elon musk in 2025?"))

print(agent.run(" Multiply age of elon musk in 2025 and 2"))


