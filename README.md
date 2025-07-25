# Jira Agent Project

This project implements a multi-agent system for managing Jira tasks, summarizing information, and sending email notifications. The system uses a supervisor agent to delegate tasks to specialized agents: a Jira agent, a summary agent, and an email agent.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running without Docker](#running-without-docker)
  - [Running with Docker](#running-with-docker)

## Features

- **Jira Integration:** Connects to Jira to fetch information about projects and issues.
- **Task Summarization:** Summarizes the retrieved Jira information.
- **Email Notifications:** Sends email notifications with the summarized information.
- **Multi-Agent System:** Uses a supervisor agent to manage the workflow between the different agents.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- Docker and Docker Compose (for running with Docker)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohana9985/Multi-Agent-Model-Jira_Agent-.git
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

## Configuration

Create a `.env` file in the root directory of the project and add the following environment variables. This file will be used for both running with and without Docker.

```
# Jira Configuration
JIRA_API_TOKEN=<your-jira-api-token>
JIRA_USERNAME=<your-jira-username>
JIRA_INSTANCE_URL=<your-jira-instance-url>

# Email Configuration
EMAIL_USER=<your-email-address>
EMAIL_PASSWORD=<your-email-password>

# LLM Configuration
MODEL_ID=<your-model-id>
MODEL_PROVIDER=<your-model-provider>

# SMTP Configuration
SMTP_HOST=<your-smtp-host>
SMTP_PORT=<your-smtp-port>
SMTP_USERNAME01=<your-smtp-username>
SMTP_PASSWORD01=<your-smtp-password>
FROM_EMAIL=<your-from-email>
```

## Usage

You can run the application either with or without Docker.

### Running without Docker

To run the supervisor agent directly, execute the following command:

```bash
langgraph dev
```
or 

```bash
langgraph dev --allow-blocking
```

The supervisor will then delegate tasks to the appropriate agents based on the provided query. For example, to get all defects in the "Learning Management syste Project", the supervisor will call the Jira agent, then the summary agent, and finally the email agent to send a notification.

### Running with Docker

To run the application using Docker Compose, first ensure that the `.env` file is correctly configured, as it will be used by the `langgraph-api` service. Then, execute the following command:

```bash
docker-compose up --build
```

This will build the Docker image and start all the services defined in the `docker-compose.yml` file, including the LangGraph API, Redis, and Postgres. The `--build` flag ensures that the image is rebuilt with any new changes.
