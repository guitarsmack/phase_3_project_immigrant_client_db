from models.__init__ import CURSOR, CONN
import countryinfo
import pycountry

# Test new device push again

class Country:

    all = {}

    def __init__( self, name, language = None, id = None ):
        self.name = name
        self.language = language
        self.id = id
    
    def __repr__(self):
        return f'<Country {self.id}: {self.name}, {self.language}>'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if len(name) > 0 and isinstance(name,str):
            country = countryinfo.CountryInfo(name)
            self._name = country.name().capitalize()
        else:
            raise Exception('Not valid country name')

    
    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self,value):
        lang_code = countryinfo.CountryInfo(self._name).languages()[0]
        language = pycountry.languages.get(alpha_2=lang_code).name
        self._language = language
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS country (
        id INTEGER PRIMARY KEY,
        name TEXT,
        language TEXT
        )
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS country"""

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name):
        country = cls(name)
        country.save()
        return country
    
    def save(self):
        sql = """
        INSERT INTO country (name,language) VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name,self.language))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def instance_from_db(cls,row):

        country = cls.all.get(row[0])

        if country:
            country.name = row[1]
            country.language = row[2]
        else:
            country = cls(row[1],row[2])
            country.id = row[0]
            cls.all[country.id] = country
        
        return country
    
    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM country
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def check_valid_id(cls,id_):
        sql = """
        SELECT * FROM country WHERE id = ?
        """

        row = CURSOR.execute(sql, (id_,)).fetchone()
        return row[0] if row else None
    
    @classmethod
    def get_id_by_name(cls,name):
        sql = """
        SELECT * FROM country WHERE name = ?
        """
        
        row = CURSOR.execute(sql, (name.capitalize(),)).fetchone()

        return row[0] if row else None
    
    @classmethod
    def get_by_id(cls,id_):
        sql = """
        SELECT * FROM country WHERE id = ?
        """

        row = CURSOR.execute(sql, (id_,)).fetchone()
        return cls.instance_from_db(row) if row else None

    
    
    def delete(self):
        sql = """
        DELETE FROM country WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
        

    @classmethod
    def get_countries_by_language(cls,lang):
        sql = """
        SELECT * FROM country WHERE language = ?
        """

        rows = CURSOR.execute(sql, (lang,)).fetchall()
        return [ row[0] for row in rows ]
    
    @classmethod
    def get_by_language(cls,lang):
        sql = """
        SELECT * FROM country WHERE language = ?
        """

        rows = CURSOR.execute(sql, (lang,)).fetchall()
        return [ cls.instance_from_db(row) for row in rows ]
