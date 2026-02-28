import phonenumbers
from phonenumbers import geocoder, carrier
import requests

def melacak_nomor (nomor):
    try:
        nomor = phonenumbers.parse(nomor)

        if not phonenumbers.is_valid_number(nomor):
            return "Nomor tidak valid"
        
        location = geocoder.description_for_number(nomor, "id")

        provider = carrier.name_for_number(nomor, "id")

        return f"Nomor ini berasal dari {location} dan di miliki oleh {provider}"
    except Exception as e:
        return f"Error: {e}"

def get_location_from_coordinates(lat, lng):
    api_key = 'YOUR_OPENCAGE_API_KEY'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={lat}+{lng}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data['results']:
        return data['results'][0]['formatted']
    else:
        return "Lokasi tidak ditemukan"
    

lat, lng = 51.5074, -0.1278  # Coordinates for London
location = get_location_from_coordinates(lat, lng)print(location)