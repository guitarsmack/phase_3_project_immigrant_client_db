# lib/helpers.py
from models.client import Client
from models.country import Country
import random

def exit_program():
    farewell = ["Adiós","Sayonara","Au revoir","Dasvidaniya","Ma’a salama", "Zàijiàn","Arrivederci","Namaste"]
    print(random.choice(farewell),"(Goodbye!)")
    exit()

def create_client():
    name = input("New client's name: ")
    country = input("Where is client from: ")
    try:
        client = Client.create(name,country)
        print(f"Success {client}")
    except Exception as exc:
        print("Error: ", exc)


def get_clients():
    clients = Client.get_all()
    return [ print(client) for client in clients]

def get_client_by_id():
    id_ = input("Enter client ID to search by: ")
    if client := Client.get_by_id(id_):
        print(client)
    else:
        print(f"Client ID {id_} not found")

def delete_client_by_id():
    id_ = input("Enter client ID to remove from database: ")
    if client := Client.get_by_id(id_):
        client.delete()
        print(f"Client {id_}, {client.name} deleted")
    else:
        print(f"Client {id_} not found")

def get_clients_by_country():
    origin = input("Enter country to get clients from there: ")
    if clients := Client.get_by_country(origin):
        try:
            [ print(client) for client in clients ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No clients from {origin}")

def get_clients_by_language():
    language = input("Enter language to get clients who speak it: ")
    if clients := Client.get_by_language(language):
        try:
            [ print(client) for client in clients ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No clients who speak {language}")
    
def create_country():
    name = input("What country to add: ")
    try :
        country = Country.create(name)
        print(f"Success: {country}")
    except Exception as exc:
        print("Error: ", exc)
    
def delete_country_by_id():
    id_ = input("Enter country ID to remove from database: ")
    if country := Country.get_by_id(id_):
        country.delete()
        print(f"Origin {id_}, {country.name} deleted")
    else:
        print(f"Origin {id_} not found")
    
def get_countries():
    countries = Country.get_all()
    return [print(country) for country in countries]

def get_country_by_id():
    id_ = input("Enter country ID to search by: ")
    if country := Country.get_by_id(id_):
        print(country)
    else:
        print(f"Country ID {id_} not found")
    
def get_countries_by_language():
    language = input("Enter language to get countries who primarily speak it: ").capitalize()
    if countries := Country.get_by_language(language):
        try:
            [ print(country) for country in countries ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No countries who speak {language}")

