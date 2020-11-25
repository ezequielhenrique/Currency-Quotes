import requests
import json
from tkinter import messagebox


def get_quotes():
    try:
        response = requests.get('https://economia.awesomeapi.com.br/json/all')
        response.raise_for_status()

        quotation_data = json.loads(response.text)

        return quotation_data

    except requests.exceptions.ConnectionError:
        return messagebox.showerror('Error', 'Sem conexão')
    except requests.exceptions.HTTPError:
        return messagebox.showerror('Error', '404 Client Error: URL not found')
