from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(num1: float, num2: float) -> str:
    """Used to perform arithmatic operations"""
    return f"The sum of {num1} and {num2} is {num1+num2}"

def main():

    model = ChatOpenAI(temperature=0)
    tools = [calculator]
    agent_excutor = create_react_agent(model,tools)
    print("Hi, I am your AI assistant, tell me what I can help you with or type quit to exit ")

    while True:

        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssisstant: ", end="")

        for chunk in agent_excutor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()


if __name__ == "__main__":
    main()
            
