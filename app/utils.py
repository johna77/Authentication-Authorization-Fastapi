# Hash and Verify the password and Calculator Program
from passlib.context import CryptContext
import requests
api_key = 

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_data(place, forecast_data, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nr_valus = 8 * forecast_data
    filtered_data = filtered_data[:nr_valus]
    return filtered_data
