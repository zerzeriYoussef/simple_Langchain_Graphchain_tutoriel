from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import os

load_dotenv()

def langchain_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Setup Wikipedia tool
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    
    # Create tools list
    tools = [wikipedia]
    
    # Create agent using langgraph
    agent = create_react_agent(llm, tools)
    
    # Run the agent - in LangChain v1.0+, the graph is invoked directly
    result = agent.invoke({"messages": [HumanMessage(content="What is the average age of a dog?")]})
    return result['messages'][-1].content

def generate_pet_name():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    prompt = PromptTemplate(
        input_variables=["animal"],
        template="Generate a name for a {animal}"
    )
    chain = prompt | llm
    return chain.invoke({"animal": "dog"})

# Test the agent
print(langchain_agent())    