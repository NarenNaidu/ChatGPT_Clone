@echo off
echo Starting Gemini Chat App...
echo.
echo Make sure your GEMINI_API_KEY is set in the .env file
echo Opening browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "C:\Source_Code\Python\ChatGPT_Clone"
call "myenv\Scripts\activate.bat"
streamlit run streamlit_demo.py
