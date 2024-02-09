import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY=os.environ['OPENAI_API_KEY']

PINECONE_API_KEY=os.environ['PINECONE_API_KEY']
PINECONE_CLOUD=os.environ['PINECONE_CLOUD']
PINECONE_INDEX_NAME='hackerearth'
PINECONE_DIMENSION=1536
PINECONE_METRICS='cosine'

CHUNK_SIZE = 100
CHUNK_OVERLAP = 20

DEFAULT_MODEL_NAME="gpt-3.5-turbo"
DEFAULT_MODEL_TEMPERATURE=0.5


FIRST_ASSISTANT_MESSAGE = "Hi, welcome to HackerEarth! I'm your AI assistant and I can answer any questions you have about HackerEarth. How can I help you today? 😊"
SYSTEM_MESSAGE = """
    You are a really profession sales person for HackerEarth with intention to sell HackerEarth's product.
    You job is help our customers by effectively answering questions about the company, encourage users to sign up for a demo, and capture their contact details for further follow-up.
    Always answer questions by mentioning HackerEarth in your mesassage.
    If user asks questions on unrelated topics, ask them to ask questions around HackerEarth!
    Be friendly in nature. Prefer answering questions in few lines if possible.
"""
