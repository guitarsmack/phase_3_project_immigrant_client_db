from models.__init__ import CURSOR, CONN
import countryinfo
import pycountry

class Countries:

    all = {}

    def __init__( self, name, language = None, id = None ):
        self.name = name
        self.language = language
        self.id = id
    
    def __repr__(self):
        return f'<Country {self.name}: {self.language}>'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        country = countryinfo.CountryInfo(name)
        self._name = country.name().capitalize()
    
    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self,value):
        lang_code = countryinfo.CountryInfo(self._name).languages()[0]
        language = pycountry.languages.get(alpha_2=lang_code).name
        answer = input(f"Does {self._name}'s primary language being {language} sound correct?(y/n) ")
        if answer.lower() == "y":
            self._language = language
        elif answer.lower() == "n":
            language = input("I'm sorry. Please enter this country's primary language? ")
            self._language = language
    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        language TEXT
        )
        """

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS countries"""

        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name):
        country = cls(name)
        country.save()
        return country
    
    def save(self):
        sql = """
        INSERT INTO countries (name,language) VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name,self.language))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self