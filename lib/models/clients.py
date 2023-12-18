from models.__init__ import CURSOR, CONN
from models.countries import Countries
import datetime as dt
import countryinfo

class Clients:

    all = {}

    def __init__(self, name, origin, id = None):
        self.id = id
        self.name = name
        self.date_joined = dt.datetime.now().strftime('%m-%d-%Y')
        self.origin = origin
    
    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.origin}, {self.date_joined}>"
    
      
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) > 0:
            self._name = value
        else:
            raise Exception('Name either not string or too short')
    
    @property
    def origin(self):
        return self._origin
        
    @origin.setter
    def origin(self, value):
        country = countryinfo.CountryInfo(value)
        country_id = Countries.get_id_by_name(country.name().capitalize())
        if country_id:
            self._origin = country_id
        else:
            raise ValueError('Sorry, country not yet in database.')


    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        origin INTEGER,
        date_joined TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS clients
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name,origin):
        client = cls(name,origin)
        client.save()
        return client
    
    def save(self):
        sql = """
        INSERT INTO clients (name,origin,date_joined) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name,self.origin,self.date_joined))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls,row):

        client = cls.all.get(row[0])

        if client:
            client.name = row[1]
            client.origin = row[2]
            client.date_joined = row[3]
        else:
            client = cls(row[1],row[2])
            client.id = row[0]
            cls.all[client.id] = client
        
        return client
    
    @classmethod
    def get_all(cls):
        sql = """
        Select * FROM clients
        """

        all_rows = CURSOR.execute(sql).fetchall()
        return all_rows
    
    @classmethod
    def get_by_id(cls,id):

        sql = """
        SELECT * FROM clients WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def delete_by_id(self,id):
        sql = """
        DELETE FROM clients WHERE id = ?
        """

        CURSOR.execute(sql, (id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None






