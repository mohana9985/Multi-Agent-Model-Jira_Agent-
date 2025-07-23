# Jira Agent Project

This project implements a multi-agent system for managing Jira tasks, summarizing information, and sending email notifications. The system uses a supervisor agent to delegate tasks to specialized agents: a Jira agent, a summary agent, and an email agent.

## Features

- **Jira Integration:** Connects to Jira to fetch information about projects and issues.
- **Task Summarization:** Summarizes the retrieved Jira information.
- **Email Notifications:** Sends email notifications with the summarized information.
- **Multi-Agent System:** Uses a supervisor agent to manage the workflow between the different agents.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/jira-agents.git
   cd jira-agents
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory of the project and add the following variables:
   ```
   JIRA_API_TOKEN=<your-jira-api-token>
   JIRA_USERNAME=<your-jira-username>
   JIRA_INSTANCE_URL=<your-jira-instance-url>
   EMAIL_USER=<your-email-address>
   EMAIL_PASSWORD=<your-email-password>
   ```

## Usage

To run the supervisor agent, execute the following command:
```bash
python supervisor.py
```

The supervisor will then delegate tasks to the appropriate agents based on the provided query. For example, to get all defects in the "Learning Management syste Project", the supervisor will call the Jira agent, then the summary agent, and finally the email agent to send a notification.
