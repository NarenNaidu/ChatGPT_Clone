"""
Streamlit Chat App using Google Gemini LLM
"""

import streamlit as st
import os
from dotenv import load_dotenv
from my_utlis import get_llm_response

# Load environment variables
load_dotenv()

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "model" not in st.session_state:
        st.session_state.model = "gemini-1.5-flash"
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = ""

def display_chat_messages():
    """Display all chat messages"""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="Gemini Chat Clone",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Gemini Chat Clone")
    st.markdown("Chat with Google's Gemini AI using PydanticAI")
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Model selection
        model_options = {
            "Gemini 1.5 Flash": "gemini-1.5-flash",
            "Gemini 1.5 Pro": "gemini-1.5-pro", 
            "Gemini 1.0 Pro": "gemini-1.0-pro"
        }
        
        selected_model_name = st.selectbox(
            "Select Model:",
            options=list(model_options.keys()),
            index=0
        )
        st.session_state.model = model_options[selected_model_name]
        
        # System prompt input
        st.markdown("**System Prompt:**")
        
        # Preset system prompts
        preset_prompts = {
            "Default": "",
            "Programming Assistant": "You are a helpful programming assistant who explains concepts clearly and provides working code examples.",
            "Creative Writer": "You are a creative writer who helps with storytelling, poetry, and creative content.",
            "Academic Tutor": "You are an academic tutor who explains complex topics in simple terms with examples.",
            "Business Advisor": "You are a business consultant who provides practical advice and strategic insights.",
            "Friendly Helper": "You are a friendly and encouraging assistant who provides helpful answers with a positive tone."
        }
        
        selected_preset = st.selectbox(
            "Choose a preset or create custom:",
            options=list(preset_prompts.keys()),
            index=0
        )
        
        # Use preset or custom system prompt
        if selected_preset != "Default":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = st.session_state.system_prompt
        
        system_prompt = st.text_area(
            "System prompt:",
            value=default_prompt,
            placeholder="e.g., You are a helpful programming assistant who explains concepts clearly...",
            height=100,
            help="Define how the AI should behave and respond"
        )
        st.session_state.system_prompt = system_prompt
        
        # API Key status
        if os.getenv("GEMINI_API_KEY"):
            st.success("✅ API Key loaded")
        else:
            st.error("❌ API Key not found")
            st.markdown("Please set your `GEMINI_API_KEY` in the `.env` file")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()
        
        # Chat statistics
        st.markdown("---")
        st.markdown(f"**Messages:** {len(st.session_state.messages)}")
        st.markdown(f"**Model:** {selected_model_name}")
    
    # Main chat interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Display chat messages
        display_chat_messages()
        
        # Chat input
        if prompt := st.chat_input("Type your message here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Get AI response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        # Call the LLM using our utility function with system prompt
                        response = get_llm_response(
                            prompt, 
                            st.session_state.model, 
                            st.session_state.system_prompt if st.session_state.system_prompt.strip() else None
                        )
                        
                        # Display response
                        st.markdown(response)
                        
                        # Add assistant response to chat history
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": response
                        })
                        
                    except Exception as e:
                        error_msg = f"Error: {str(e)}"
                        st.error(error_msg)
                        
                        # Add error to chat history
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": error_msg
                        })
    
    with col2:
        # Tips and information
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Ask questions about any topic
        - Request code examples
        - Get explanations and tutorials
        - The AI remembers your conversation
        """)
        
        st.markdown("### 🔧 Models")
        st.markdown("""
        - **Flash**: Fast responses, good for general queries
        - **Pro**: More capable, better for complex tasks
        - **1.0 Pro**: Legacy model
        """)
        
        # Example prompts
        st.markdown("### 🌟 Example Prompts")
        example_prompts = [
            "Explain quantum computing",
            "Write a Python function to sort a list", 
            "What's the difference between AI and ML?",
            "Create a simple HTML webpage",
            "Explain how blockchain works"
        ]
        
        for prompt in example_prompts:
            if st.button(f"💭 {prompt}", key=f"example_{prompt}", use_container_width=True):
                # Add the example prompt to chat
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()

if __name__ == "__main__":
    main()
