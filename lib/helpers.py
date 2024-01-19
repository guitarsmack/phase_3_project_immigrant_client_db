# lib/helpers.py
from models.clients import Clients
from models.countries import Countries
import random

def exit_program():
    farewell = ["Adiós","Sayonara","Au revoir","Dasvidaniya","Ma’a salama", "Zàijiàn","Arrivederci","Namaste"]
    print(random.choice(farewell),"(Goodbye!)")
    exit()

def create_client():
    name = input("New client's name: ")
    origin = input("Where is client from: ")
    try:
        client = Clients.create(name,origin)
        print(f"Success {client}")
    except Exception as exc:
        print("Error: ", exc)


def get_clients():
    clients = Clients.get_all()
    return [ print(client) for client in clients]

def get_client_by_id():
    id_ = input("Enter client ID to search by: ")
    if client := Clients.get_by_id(id_):
        print(client)
    else:
        print(f"Client ID {id_} not found")

def delete_client_by_id():
    id_ = input("Enter client ID to remove from database: ")
    if client := Clients.get_by_id(id_):
        client.delete()
        print(f"Client {id_}, {client.name} deleted")
    else:
        print(f"Client {id_} not found")

def get_clients_by_origin():
    origin = input("Enter country to get clients from there: ")
    if clients := Clients.get_by_origin(origin):
        try:
            [ print(client) for client in clients ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No clients from {origin}")

def get_clients_by_language():
    language = input("Enter language to get clients who speak it: ")
    if clients := Clients.get_by_language(language):
        try:
            [ print(client) for client in clients ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No clients who speak {language}")
    
def create_country():
    name = input("What country to add: ")
    try :
        country = Countries.create(name)
        print(f"Success: {country}")
    except Exception as exc:
        print("Error: ", exc)
    
def delete_country_by_id():
    id_ = input("Enter country ID to remove from database: ")
    if country := Countries.get_by_id(id_):
        country.delete()
        print(f"Origin {id_}, {country.name} deleted")
    else:
        print(f"Origin {id_} not found")
    
def get_countries():
    countries = Countries.get_all()
    return [print(country) for country in countries]

def get_country_by_id():
    id_ = input("Enter country ID to search by: ")
    if country := Countries.get_by_id(id_):
        print(country)
    else:
        print(f"Country ID {id_} not found")
    
def get_countries_by_language():
    language = input("Enter language to get countries who primarily speak it: ").capitalize()
    if countries := Countries.get_by_language(language):
        try:
            [ print(country) for country in countries ]
        except Exception as exc:
            print("Exception: ", exc)
    else:
        print(f"No countries who speak {language}")

