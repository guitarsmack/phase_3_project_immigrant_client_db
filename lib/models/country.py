from models.__init__ import CURSOR, CONN

class Country:

    all = {}

    def __init__( self, name, language, id = None ):
        self.name = name
        self.language = language
    
    def __repr__(self):
        return f'<Country {self.name}: {self.language}>'
    
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
    def create(cls,name,language):
        country = cls(name,language)
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