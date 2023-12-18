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

    Clients.create('Sierra','Brazil')

    Countries.create('Brazil')

seed_database()

ipdb.set_trace()
