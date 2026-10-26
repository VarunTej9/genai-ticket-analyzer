
# AI Customer Support Ticket Analyzer

A beginner-friendly Generative AI project that
automatically analyzes customer complaints using
Google Gemini API and Python.

## Features

- Customer complaint classification
- Automatic priority detection
- AI-generated ticket summaries
- Suggested customer support responses
- Structured JSON output using Pydantic

## Tech Stack

- Python
- Google Gemini API
- Pydantic
- Prompt Engineering
- Google GenAI SDK

## System Architecture

Customer Complaint
       |
       v
Python Application
       |
       v
System Prompt + Complaint
       |
       v
Google Gemini LLM
       |
       v
Structured JSON Response
       |
       v
Pydantic Validation
       |
       v
Category + Priority + Summary + Reply

## Example Input

My application has crashed and none of
our employees can access it.

## Example Output

Category: Technical
Priority: High

Summary:
The application has crashed, preventing
all employees from accessing it.

Suggested Reply:
We apologize for the disruption.
Our team will investigate the issue.

## How to Run

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Create a .env file.
4. Add your GEMINI_API_KEY.
5. Run:

   python main.py

## Concepts Learned

- LLM API integration
- System prompts
- Structured output
- Text classification
- Generative text responses
- Basic GenAI workflow design

## Future Improvements

- ASP.NET Core Web API integration
- Automated ticket routing
- Ticket history database
- Web-based user interface
