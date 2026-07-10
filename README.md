# HobbyFi AI Copilot

An AI-powered vendor copilot built for the HobbyFi AI Engineer Assessment.

The copilot helps vendors retrieve business insights, manage customers, and answer policy-related questions using AI-powered tool calling and Retrieval-Augmented Generation (RAG).

---

## Features

### Analytics
- Get today's revenue
- Business analytics

### CRM
- View trial users
- Extend memberships (requires approval)

### Knowledge Base (RAG)
- Cancellation Policy
- Refund Policy
- Booking Policy
- FAQs

### AI Features
- Mastra Agent
- Tool Calling
- OpenRouter LLM
- Ollama + LlamaIndex RAG

---

## Tech Stack

### AI
- Mastra
- OpenRouter (GPT-4.1 Mini)
- Ollama
- LlamaIndex

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL

### Database
- PostgreSQL

### Languages
- TypeScript
- Python

---

## Architecture

```
                User
                  │
                  ▼
        Mastra Supervisor Agent
                  │
     ┌────────────┼─────────────┐
     ▼            ▼             ▼
 Revenue Tool  CRM Tool   Knowledge Tool
     │            │             │
     ▼            ▼             ▼
          FastAPI Backend
               │
      ┌────────┴────────┐
      ▼                 ▼
 PostgreSQL      Ollama + LlamaIndex
```

---

## Project Structure

```
backend/
│
├── api/
├── services/
├── repositories/
├── models/
├── knowledge/
└── database/

mastra/
│
├── agents/
├── tools/
├── config/
└── services/
```

---

## AI Tool Flow

### Revenue

User
↓
Supervisor Agent
↓
Revenue Tool
↓
FastAPI
↓
PostgreSQL

---

### Trial Users

User
↓
Supervisor Agent
↓
Trial Users Tool
↓
FastAPI
↓
PostgreSQL

---

### Membership Update

User
↓
Supervisor Agent
↓
Ask for Confirmation
↓
Membership Tool
↓
FastAPI
↓
PostgreSQL

---

### Knowledge

User
↓
Supervisor Agent
↓
Knowledge Tool
↓
FastAPI
↓
LlamaIndex
↓
Ollama

---

## Example Prompts

### Revenue

```
What is today's revenue?
```

### Trial Users

```
Show badminton trial users.
```

### Membership

```
Extend Rahul's membership by 30 days.
```

### Knowledge

```
What is the cancellation policy?
```

---

## Running the Project

### Backend

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

### Mastra

```bash
cd mastra
npm install
npm run dev
```

---

## APIs

### Analytics

```
GET /analytics/revenue
```

### Trial Users

```
GET /users/trial
```

### Membership

```
POST /membership/extend
```

### Knowledge

```
POST /knowledge/ask
```

---

## AI Workflow

- User asks a question.
- Supervisor Agent selects the correct tool.
- Tool calls the FastAPI backend.
- Backend fetches data from PostgreSQL or the Knowledge Base.
- Response is returned to the user.

---

## Future Improvements

- Persistent approval workflow
- Multi-agent orchestration
- Authentication
- Conversation memory
- Production deployment