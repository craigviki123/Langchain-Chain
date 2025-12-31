import os

from dotenv import load_dotenv

load_dotenv()
from langchain import ChatOpenAI, ChatVertexAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

if __name__ == "__main__":
    openai = ChatOpenAI(model_name="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    vertex = ChatVertexAI(
        model_name="gemini-1.5-flash", api_key=os.getenv("VERTEX_API_KEY")
    )
    prompt = ChatPromptTemplate.from_template("What is the capital of {country}?")
    chain = LLMChain(llm=openai, prompt=prompt)
    print(chain.run("India"))
