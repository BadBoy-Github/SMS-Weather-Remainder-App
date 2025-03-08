
import os
import requests
from twilio.rest import Client

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_API_KEY")

params = {
    "lat": 11.368007,
    "lon": 77.928786,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
data = response.json()

sms = True

for i in range(4):
    weather_id = data["list"][i]["weather"][0]["id"]
    if int(weather_id) < 700:
        message = "It's going to rain today. Remember to bring an Umbrella! ☔"
    else:
        message = "It's going to be a normal day. Enjoy your day!😉"

if sms:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_="+18142595432",
        to="+919842852121"
    )
    print(message.status)