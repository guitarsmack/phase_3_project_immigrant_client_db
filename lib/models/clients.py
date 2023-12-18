from models.__init__ import CURSOR, CONN
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
    def origin(self,value):
        country = countryinfo.CountryInfo(value)
        if country:
            self._origin = country.name().capitalize()
        else:
            raise Exception('Not valid country')

    @classmethod
    def create_table(cls):
        """Creates a client table, primarily for the seed file"""
        sql = """
        CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        origin TEXT,
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

    # @classmethod
    # def instance_from_db(cls,row):
    #     client = cls.all.get(row[0])

        # if client:
    
    @classmethod
    def get_all(cls):
        sql = """
        Select * FROM clients
        """

        all_rows = CURSOR.execute(sql).fetchall()
        return all_rows




