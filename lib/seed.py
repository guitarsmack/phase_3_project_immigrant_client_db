from models.__init__ import CONN, CURSOR
from models.clients import Clients
from models.countries import Countries

def seed_database():
    Clients.drop_table()
    Countries.drop_table()

    Clients.create_table()
    Countries.create_table()

    
    Countries.create('Brazil')
    Clients.create('Sierra','Brazil')


seed_database()
print("Sedded")