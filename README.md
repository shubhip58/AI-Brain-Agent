# AI Agent Brain (FastAPI)

## Setup

1. Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run server
uvicorn main:app --reload

API will run at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

## Test Prompts

POST /agent/query

### Calculator
{
  "prompt": "What is 10 plus 5?"
}

### Save Memory
{
  "prompt": "Remember my cat's name is Fluffy"
}

### Get Memory
{
  "prompt": "What is my cat's name?"
}

## Security Note
Calculator avoids using eval() and instead parses expressions using Python AST for safety.