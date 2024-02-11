#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from lib.models.client import Client
from lib.models.country import Country
import countryinfo
import pycountry

import ipdb

def seed_database():
    Client.drop_table()
    Country.drop_table()

    Client.create_table()
    Country.create_table()

    
    Country.create('Brazil')
    Country.create('France')
    Country.create('United States')
    Country.create('Mexico')
    Country.create('Cuba')
    Country.create('Honduras')

    Client.create('Connor','France')
    Client.create('Vincent','France')
    Client.create('Sierra','Brazil')
    Client.create('Sonya','Brazil')
    Client.create('Julio','Brazil')
    Client.create('Luis','Brazil')
    Client.create('Bob','United States')
    Client.create('Jose','Mexico')
    Client.create('Carolina','Mexico')
    Client.create('Santana','Mexico')
    Client.create('Alex','Honduras')
    Client.create('Philip','Honduras')
    Client.create('Julio','Mexico')
    Client.create('Luis','Cuba')
    Client.create('Fidel','Cuba')
    Client.create('Che','Cuba')



seed_database()

ipdb.set_trace()
