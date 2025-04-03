from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import time

# import ollama

# constants

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

# set up environment

load_dotenv()
openai = OpenAI()

question = """
 Please explain what this code does and why:
 yield from {book.get("author") for book in books if book.get("author")}
 """
# Get user input first
my_question = input("Please enter your question:")

# prompts

system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + my_question

# messages

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

# Get gpt-4o-mini to answer, with streaming
stream = openai.chat.completions.create(model=MODEL_GPT, messages=messages, stream=True)

# Print response in real-time
print("\nAI Response:")
response = ""
for chunk in stream:
    content = chunk.choices[0].delta.content or ''
    response += content
    print(content, end='', flush=True)
    time.sleep(0.01)  # Small delay to make streaming more visible

print("\n\nFull response:\n")
print(response)
