# PowerShell script to run the Streamlit Gemini Chat App

Write-Host "Starting Gemini Chat App..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure your GEMINI_API_KEY is set in the .env file" -ForegroundColor Yellow
Write-Host "Opening browser at http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Change to app directory
Set-Location "C:\Source_Code\Python\ChatGPT_Clone"

# Activate virtual environment
& ".\myenv\Scripts\Activate.ps1"

# Run Streamlit app
streamlit run streamlit_demo.py
