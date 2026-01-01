import os
import warnings

# Suppress various warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from dotenv import load_dotenv

load_dotenv()
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate


if __name__ == "__main__":
    openai = ChatVertexAI(model="gemini-2.5-pro", project="dit06-insight-us-idp", location="us-east1")
    prompt = PromptTemplate(input_variables=["country"], template="What is the capital of {country}?")
    chain = prompt | openai
    response = chain.invoke({"country": "India"})
    print("|--------------------------------------------|")
    print(response.content)
    print("|--------------------------------------------|")
    