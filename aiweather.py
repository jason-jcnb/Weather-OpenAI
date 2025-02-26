
import requests
import tkinter as tk
from tkinter import messagebox
import time
import threading
import openai

API_KEY = "kindly Use Your Own OpenWeatherMap key"
OPENAI_API_KEY = "kindlyUseYourOwnOpenAIkey"

openai.api_key = OPENAI_API_KEY

def get_weather(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        temperature_k = data["main"]["temp"]
        temperature_c = round(temperature_k - 273.15, 2)
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_report = (
            f"🌍 City: {city}\n"
            f"🌡 Temperature: {temperature_c}°C\n"
            f"☁ Weather: {weather_desc.capitalize()}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind_speed} m/s\n"
            "--------------------------"
        )

        return weather_report
    else:
        return f"⚠ Error: {data['message']}"

def get_ai_report(weather_report):
    prompt = f"Summarize the following weather report:\n{weather_report}"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    ai_report = response.choices[0].text.strip()
    return ai_report

def update_weather():
    city_name = city_entry.get()
    if city_name == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    interval = int(interval_entry.get()) * 60  

    while True:
    
        weather_report = get_weather(city_name)

        ai_report = get_ai_report(weather_report)

        weather_label.config(text=weather_report)
        ai_label.config(text=ai_report)

        with open("weather_log.txt", "a") as file:
            file.write(weather_report + "\n")
            file.write(ai_report + "\n")

        time.sleep(interval)

def start_weather_thread():
    thread = threading.Thread(target=update_weather, daemon=True)
    thread.start()

root = tk.Tk()
root.title("Weather and AI Report")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()
city_entry = tk.Entry(root, width=30)
city_entry.pack()

interval_label = tk.Label(root, text="How often to check weather (in minutes)?")
interval_label.pack()
interval_entry = tk.Entry(root, width=10)
interval_entry.pack()

start_button = tk.Button(root, text="Start Weather Updates", command=start_weather_thread)
start_button.pack()

weather_label = tk.Label(root, text="Weather will be displayed here", width=50, height=10, anchor="w", justify="left")
weather_label.pack()

ai_label = tk.Label(root, text="AI summary will appear here", width=50, height=10, anchor="w", justify="left")
ai_label.pack()

root.mainloop()