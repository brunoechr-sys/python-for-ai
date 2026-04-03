
from pathlib import Path
from dotenv import load_dotenv
import os
import requests

base = Path(__file__).resolve().parent
dotenv_path = base / ".env"
load_dotenv(dotenv_path=dotenv_path, override=True)

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_URL', 'default.db')

print(f"Using API key: {api_key}")
print(f"Using database: {database}")


# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
print(f"The current temperature in Paris is: {data['current']['temperature_2m']}°C")

# Debug info
print("cwd:", os.getcwd())
print("script path:", Path(__file__).resolve().parent)
print("env path exists:", Path(".env").exists())
print("env file content:")
print(Path(".env").read_text())