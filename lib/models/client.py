from models.__init__ import CURSOR, CONN
from models.country import Country
import datetime as dt
import countryinfo

class Client:

    all = {}

    def __init__(self, name, country_id, id = None):
        self.id = id
        self.name = name
        self.date_joined = dt.datetime.now().strftime('%m-%d-%Y')
        self.country_id = country_id
    
    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.country_id}, {self.date_joined}>"
    
      
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
    def country_id(self):
        return self._country_id
    

    @country_id.setter
    def country_id(self, value):
        if isinstance(value,int) :
            id_ =Country.check_valid_id(str(value))
            self._country_id = id_
        else:
            country = countryinfo.CountryInfo(value)
            country = Country.get_id_by_name(country.name().capitalize())
            if country:
                self._country_id = country
            else:
                raise ValueError('Sorry, country not yet in database.')



    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS client (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country_id INTEGER,
        date_joined TEXT,
        FOREIGN KEY (country_id) REFERENCES country(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS client
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name,country):
        client = cls(name,country)
        client.save()
        return client
    
    def save(self):
        sql = """
        INSERT INTO client (name,country_id,date_joined) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name,self.country_id,self.date_joined))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls,row):

        client = cls.all.get(row[0])

        if client:
            client.name = row[1]
            client.country = row[2]
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


    def delete(self):
        sql = """
        DELETE FROM clients WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_by_country(cls,country):
        sql = """
        SELECT * FROM clients WHERE origin = ?
        """

        country_id = Country.get_id_by_name(country)

        rows = CURSOR.execute(sql, (country_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def get_by_language(cls,lang):
        country_list = Country.get_countries_by_language(lang.capitalize())
        country_string = ', '.join('?' * len(country_list))

        sql = f"SELECT * FROM clients WHERE origin IN ({country_string})"
        rows = CURSOR.execute(sql, country_list).fetchall()
        return [ cls.instance_from_db(row) for row in rows ]






