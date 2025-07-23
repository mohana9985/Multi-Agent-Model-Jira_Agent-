import os 
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from tool.llm import get_llm
from tool.state import JiraAgentState
from langchain.chat_models.base import BaseChatModel
from langgraph.graph.state import CompiledStateGraph

load_dotenv()

def get_summary(llm: BaseChatModel) -> CompiledStateGraph:
    """This method returns the compiled summary agent."""

    summary_agent = create_react_agent(
        name= "summary_agent",
        model= llm,
        tools=[],
        prompt="You are a helpful assistant in summarizing information.",
        state_schema=JiraAgentState
    )

    return summary_agent
    