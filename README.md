# AgentForge Version 3

AgentForge V3 creates a team of specialized local AI agents, runs them in parallel with Ollama, and uses a synthesizer to combine their work.

## Setup

1. Install Ollama.
2. Download the model:

```powershell
ollama pull qwen3:4b
```

3. Create and activate a virtual environment.
4. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

5. Copy `.env.example` to `.env`.
6. Run:

```powershell
python app.py
```

## Initial test

Team description:

```text
Create a software product team with a product planner, Python architect, testing specialist, and documentation writer.
```

Task:

```text
Design a simple personal expense tracker application and provide an implementation plan.
```

## Current limitation

No live web-search tool is implemented. Generated agents are required to leave their tools lists empty and must not claim current online research.
