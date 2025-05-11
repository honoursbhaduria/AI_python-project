

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

@tool
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b
@tool
def calculate_difference(a: int, b: int) -> int:    
    """Calculate the difference of two numbers."""
    return a - b
@tool
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers."""
    return a * b
@tool
def calculate_quotient(a: int, b: int) -> float:
    """Calculate the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
@tool
def calculate_power(base: int, exponent: int) -> int:
    """Calculate the power of a number."""
    return base ** exponent

@tool
def calculate_average(numbers: list) -> float:  
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers is empty.")
    return sum(numbers) / len(numbers)


load_dotenv()

def main():
    # Initialize Gemini model with your API key
    model = ChatGoogleGenerativeAI(
        model="gemini-pro",  
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    tools = [calculate_sum,calculate_average,calculate_difference,calculate_product,calculate_quotient,calculate_power,]
    agent_executor = create_react_agent(model, tools)

    print("Welcome to AI Helper (Gemini version)!")
    print("You can ask me anything, and I will try to help you.")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("\nAssistant:", end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "message" in chunk["agent"]:
                for message in chunk["agent"]["message"]:
                    print(message["content"], end="", flush=True)
        print()

if __name__ == "__main__":
    main()


