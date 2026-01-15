#!/bin/bash

echo "Starting Moonshot AI Chatbot Web Interface..."
echo "Make sure you have set your MOONSHOT_API_KEY environment variable"
echo "or enter it in the web interface sidebar."
echo ""
echo "Opening the app at http://localhost:8501"
echo ""
streamlit run app.py --server.port 8501 --server.address 0.0.0.0