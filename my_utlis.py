"""
Simple utilities for ChatGPT clone using PydanticAI with Google Gemini
"""

import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel

# Load environment variables from .env file
load_dotenv()


def get_llm_response(prompt: str, model_name: str = "gemini-1.5-flash", system_prompt: str = None) -> str:
    """
    Get a response from Google Gemini LLM using PydanticAI.
    
    Args:
        prompt (str): The user's prompt/question
        model_name (str): The Gemini model to use (default: gemini-1.5-flash)
                         Options: gemini-1.5-pro, gemini-1.5-flash, gemini-1.0-pro
        system_prompt (str, optional): System prompt to set context for the AI
        
    Returns:
        str: The LLM's response
        
    Raises:
        ValueError: If GEMINI_API_KEY environment variable is not set
        Exception: If there's an error communicating with the LLM
    """
    # Check if Gemini API key is set
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY environment variable must be set")
    
    try:
        # Create the Google model
        model = GoogleModel(model_name)
        
        # Create an agent with the model and optional system prompt
        if system_prompt:
            agent = Agent(model=model, system_prompt=system_prompt)
        else:
            agent = Agent(model=model)
        
        # Get the response synchronously
        response = agent.run_sync(prompt)
        
        # Return the response output
        return response.output
        
    except Exception as e:
        raise Exception(f"Error getting LLM response: {str(e)}")


def chat_with_llm(system_prompt: str = None, model_name: str = "gemini-1.5-flash") -> None:
    """
    Interactive chat function that continuously takes user input and returns LLM responses.
    
    Args:
        system_prompt (str, optional): System prompt to set context for the conversation
        model_name (str): The Gemini model to use (default: gemini-1.5-flash)
    """
    print("Gemini Chat Clone - Type 'quit' or 'exit' to end the conversation")
    print("-" * 50)
    
    # Create model and agent
    try:
        model = GoogleModel(model_name)
        
        # Create agent with optional system prompt
        if system_prompt:
            agent = Agent(model=model, system_prompt=system_prompt)
            print(f"System: {system_prompt}")
            print("-" * 50)
        else:
            agent = Agent(model=model)
            
    except Exception as e:
        print(f"Error initializing chat: {e}")
        return
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit conditions
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            if not user_input:
                continue
                
            # Get LLM response
            print("Assistant: ", end="", flush=True)
            response = agent.run_sync(user_input)
            print(response.output)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Simple example
        response = get_llm_response("What is Python?")
        print("Response:", response)
        
        # Example with system prompt
        system_prompt = "You are a helpful programming assistant who explains " \
        "concepts clearly and concisely. Please respond in Mumbaikar language. "
        response_with_system = get_llm_response(
            "What is Python?", 
            system_prompt=system_prompt
        )
        print("\nResponse with system prompt:", response_with_system)
        
        # Start interactive chat
        # chat_with_llm("You are a helpful programming assistant.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure to set your GEMINI_API_KEY environment variable:")
