"""
Example usage of the PydanticAI utility functions with Google Gemini
"""

import os
from dotenv import load_dotenv
from my_utlis import get_llm_response, chat_with_llm

# Load environment variables from .env file
load_dotenv()


def main():
    """Main function to demonstrate the LLM utility functions"""
    
    print("=== PydanticAI Gemini Clone Example ===\n")
    
    # Make sure to set your Gemini API key as an environment variable
    # You can do this by running: $env:GEMINI_API_KEY="your-api-key-here" in PowerShell
    
    try:
        # Example 1: Single prompt response
        print("Example 1: Single prompt response")
        print("-" * 40)
        prompt = "Explain what machine learning is in simple terms."
        response = get_llm_response(prompt)
        print(f"Prompt: {prompt}")
        print(f"Response: {response}\n")
        
        # Example 2: Using system prompt
        print("Example 2: Using system prompt")
        print("-" * 40)
        system_prompt = "You are a technical expert who explains concepts using analogies and keeps responses under 100 words."
        response_with_system = get_llm_response(
            "What is machine learning?", 
            system_prompt=system_prompt
        )
        print(f"System Prompt: {system_prompt}")
        print(f"Response: {response_with_system}\n")
        
        # Example 3: Different Gemini model
        print("Example 3: Using Gemini Pro")
        print("-" * 40)
        try:
            response_pro = get_llm_response("What's the difference between Python and JavaScript?", "gemini-1.5-pro")
            print(f"Gemini Pro Response: {response_pro}\n")
        except Exception as e:
            print(f"Gemini Pro error: {e}\n")
        
        # Example 4: Interactive chat (uncomment to use)
        print("Starting interactive chat...")
        print("(Uncomment the line below to start chatting)")
        # chat_with_llm("You are a helpful Python programming assistant.")
        
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please set your GEMINI_API_KEY in one of these ways:")
        print("1. Update the .env file in this directory with your API key")
        print("2. Set environment variable:")
        print('   PowerShell: $env:GEMINI_API_KEY="your-api-key-here"')
        print('   CMD: set GEMINI_API_KEY=your-api-key-here')
        print("\nYou can get a free API key from: https://makersuite.google.com/app/apikey")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
