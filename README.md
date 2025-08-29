# ChatGPT Clone with Google Gemini (VIBE CODING)

**THIS APP WAS VIBE_CODED in 15 MINS!

A simple ChatGPT-like interface using PydanticAI and Google's Gemini LLM.

## Setup

1. **Get a Google Gemini API Key**
   - Visit: https://makersuite.google.com/app/apikey
   - Create a free API key

2. **Configure API Key**
   - Open the `.env` file in this directory
   - Replace `your-gemini-api-key-here` with your actual API key:
     ```
     GEMINI_API_KEY=your-actual-api-key-here
     ```

3. **Install Dependencies** (if needed)
   ```powershell
   # Activate virtual environment
   .\myenv\Scripts\Activate.ps1
   
   # Install required packages (already installed in this environment)
   pip install pydantic-ai python-dotenv
   ```

## Usage

### Simple Function Call
```python
from my_utlis import get_llm_response

# Basic usage
response = get_llm_response("What is machine learning?")
print(response)

# With system prompt to set AI behavior
response = get_llm_response(
    "What is machine learning?",
    system_prompt="You are a technical expert who explains concepts using analogies."
)
print(response)

# Use a different model
response = get_llm_response("Explain Python", "gemini-1.5-pro")
print(response)
```

### Interactive Chat
```python
from my_utlis import chat_with_llm

# Start interactive chat
chat_with_llm()

# With system prompt
chat_with_llm("You are a helpful Python programming assistant.")
```

### Streamlit Web App 🌟
Run the beautiful web interface:

```powershell
# Method 1: Using the provided script
.\run_app.ps1

# Method 2: Direct command
C:/Source_Code/Python/ChatGPT_Clone/myenv/Scripts/python.exe -m streamlit run streamlit_demo.py
```

Then open your browser to `http://localhost:8501`

**Streamlit App Features:**
- 💬 Interactive chat interface
- 🎛️ Model selection (Flash, Pro, 1.0 Pro)
- 🧠 System prompt presets and custom prompts
- 📊 Chat statistics and message count
- 🗑️ Clear chat history
- 💡 Example prompts to get started
- 🔧 API key status indicator

### Run Example
```powershell
# Make sure virtual environment is activated
.\myenv\Scripts\Activate.ps1

# Run the example
python example.py
```

## Available Models
- `gemini-1.5-flash` (default) - Fast and efficient
- `gemini-1.5-pro` - More capable, slower
- `gemini-1.0-pro` - Legacy model

## Files
- `my_utlis.py` - Main utility functions
- `example.py` - Example usage
- `streamlit_demo.py` - Web chat interface using Streamlit 🌟
- `run_app.ps1` / `run_app.bat` - Scripts to launch the Streamlit app
- `.env` - Environment variables (API keys)
- `.gitignore` - Files to ignore in git (includes .env for security)

## Security Note
The `.env` file containing your API key is automatically ignored by git to keep your API key secure.
