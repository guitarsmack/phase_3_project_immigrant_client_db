#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.clients import Clients
from models.countries import Countries
import countryinfo
import pycountry

import ipdb

def seed_database():
    Clients.drop_table()
    Countries.drop_table()

    Clients.create_table()
    Countries.create_table()

    
    Countries.create('Brazil')
    Countries.create('France')
    Countries.create('United States')
    Countries.create('Mexico')
    Countries.create('Cuba')
    Countries.create('Honduras')

    Clients.create('Connor','France')
    Clients.create('Vincent','France')
    Clients.create('Sierra','Brazil')
    Clients.create('Sonya','Brazil')
    Clients.create('Julio','Brazil')
    Clients.create('Luis','Brazil')
    Clients.create('Bob','United States')
    Clients.create('Jose','Mexico')
    Clients.create('Carolina','Mexico')
    Clients.create('Santana','Mexico')
    Clients.create('Alex','Honduras')
    Clients.create('Philip','Honduras')
    Clients.create('Julio','Mexico')
    Clients.create('Luis','Cuba')
    Clients.create('Fidel','Cuba')
    Clients.create('Che','Cuba')



seed_database()

ipdb.set_trace()
