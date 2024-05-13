import requests
import json

class ApiService:
    @staticmethod
    def get_cat_facts():
        response = requests.get('https://catfact.ninja/fact')
        return json.loads(response.content.decode()) if response.status_code == 200 else None
    
    @staticmethod
    def get_user_ip():
        response = requests.get('https://api.ipify.org/?format=json')
        return json.loads(response.content.decode()) if response.status_code == 200 else None
    