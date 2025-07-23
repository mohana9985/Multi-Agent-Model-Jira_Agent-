from tool.email import individual_email_tool
from tool.llm import get_llm
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from tool.state import JiraAgentState
from dotenv import load_dotenv
from langgraph.graph.state import CompiledStateGraph
from langchain.chat_models.base import BaseChatModel

load_dotenv()

def get_email_agent(llm: BaseChatModel) -> "CompiledStateGraph":
    """This method gets the email agent."""
    tool= [individual_email_tool]
    
    email_agent= create_react_agent(
        name="email_agent",
        model= llm,
        tools= tool,
        prompt="You are an helpful assistant in sending emails.",
        state_schema= JiraAgentState)
    
    return email_agent