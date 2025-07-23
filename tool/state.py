from langgraph.prebuilt.chat_agent_executor import AgentState
from typing import Optional

class JiraAgentState(AgentState):
    """This is the state for the Jira agent.
    """

    email_ids: Optional[str]
    raw_bugs: Optional[str]
    summary: Optional[str]
    
