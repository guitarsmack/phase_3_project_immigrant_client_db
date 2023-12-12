from models.__init__ import CONN, CURSOR
from models.client import Client
from models.country import Country

def seed_database():
    Client.drop_table()
    Country.drop_table()

    Client.create_table()
    Country.create_table()

    Client.create('Sierra','Brazil')

    Country.create('Brazil','Spanish')

seed_database()
print("Sedded")