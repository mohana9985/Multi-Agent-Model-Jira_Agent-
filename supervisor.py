from langgraph_supervisor import create_supervisor
from langgraph.graph import StateGraph, START, END
from agents.jira_agent import get_jira_agent as jira_agent
from agents.summary_agent import get_summary as summary_agent
from agents.mail_agent import get_email_agent as email_agent
from tool.email import individual_email_tool
from langchain.chat_models.base import BaseChatModel
from dotenv import load_dotenv
from tool.llm import get_llm
from tool.state import JiraAgentState
from langchain.agents import AgentExecutor
from agents.jira_agent import get_jira_agent

load_dotenv()

def supervisor() -> StateGraph:
    """Creates a supervisor agent that manages other agents."""
    
    model = get_llm()
    supervisor_agent = create_supervisor(
        model=model,
        agents=[jira_agent(llm=model), summary_agent(llm=model), email_agent(llm=model)],
        prompt=(
            "You are a supervisor managing three agents:\n"
            " - 'Jira Agent': Get all defects in Learning Management syste Project.\n"
            " - 'Email Agent': Sends out daily emails.\n"
            " - 'Summary Agent': Summarizes daily work or information.\n\n"
            "Decide which agent to call based on the task. "
            "Call one agent at a time. Do not respond yourself. "
            "Just delegate the task."
        ),
        add_handoff_back_messages=True,
        output_mode="full_history",
        state_schema=JiraAgentState
        ).compile()
    
    return supervisor_agent
