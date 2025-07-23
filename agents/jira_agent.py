import os
from langchain_core.tools import tool
from langchain_community.utilities import JiraAPIWrapper
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from langgraph.prebuilt import create_react_agent
from tool.llm import get_llm
from dotenv import load_dotenv
from langchain.chat_models.base import BaseChatModel
from langgraph.graph.state import CompiledStateGraph
from tool.state import JiraAgentState

load_dotenv()

def get_jira_agent(llm: BaseChatModel) -> CompiledStateGraph:
    """This medthod gets the defaults_agents."""

    jira = JiraAPIWrapper()
    toolkit= JiraToolkit.from_jira_api_wrapper(jira)
    jira_tool= toolkit.get_tools()
    jira_agent= create_react_agent(
        name="jira_agent",
        model= llm,
        tools= jira_tool,
        prompt="You are an helpful assistant in project management activities.",
        state_schema=JiraAgentState)
    
    return jira_agent