Weather and AI Report

This Python project fetches the current weather of a given city using the OpenWeatherMap API and then provides a summary of the weather report using the OpenAI API. It displays the weather and AI-generated summary on a Tkinter-based GUI. It also logs the weather reports and AI summaries to a text file at regular intervals.

Features:
-Fetches the current weather for any city.
-Provides a summary of the weather using OpenAI's GPT-3 model.
-Allows the user to set an interval for periodic weather updates.
-Displays both the weather report and the AI-generated summary in the GUI.
-Logs the weather and AI summary to a text file (weather_log.txt).
-Built using Python, Tkinter for the GUI, and OpenWeatherMap and OpenAI APIs.


Requirements:
To run this project, you need the following Python libraries: 
-requests (for making HTTP requests to the OpenWeatherMap API)
-openai (for interacting with OpenAI's API)
-tkinter (for the GUI)


You can install the required dependencies by running: pip install requests openai



Setup

1. Clone the repository to your local machine:
git clone https://github.com/yourusername/weather-ai-report.git
cd weather-ai-report
2. Obtain an API key from OpenWeatherMap:
Go to OpenWeatherMap and create an account to get your API key.
3. Obtain an API key from OpenAI:
Go to OpenAI and sign up to get your API key.
4. Replace the placeholder keys in the code with your actual keys:
In the code, change API_KEY and OPENAI_API_KEY to your own keys.

Usage
1. Run the script:
python weather_ai_report.py
2. The application will launch a GUI with the following input fields:
City name: Enter the name of the city for which you want to check the weather.
Interval (in minutes): Set the interval for how often you want to check the weather. For example, entering 5 will check the weather every 5 minutes.
3. Click the "Start Weather Updates" button to begin fetching weather data.
4. The weather report and AI summary will be displayed in the GUI, and the information will be logged to weather_log.txt.


Files
weather_log.txt: This file logs the weather data and AI-generated summaries at regular intervals.
weather_ai_report.py: The main script that handles weather fetching, AI summarizing, and GUI creation.


Example
Here's how the weather report and AI summary will look in the GUI:
🌍 City: London
🌡 Temperature: 14.5°C
☁ Weather: Clear sky
💧 Humidity: 60%
🌬 Wind Speed: 3.1 m/s
--------------------------
AI Summary:
The weather in London is clear with a temperature of 14.5°C, moderate humidity, and a light wind. It's a good day to be outdoors!
