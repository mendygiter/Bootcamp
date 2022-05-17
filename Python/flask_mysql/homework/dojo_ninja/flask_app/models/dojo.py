from  flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

        self.ninjas = []
    
    @classmethod
    def all_dojos(cls):
        query = 'SELECT * FROM dojos;'

        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []

        for row in results:
            dojos.append(cls(row))
        return dojos


    #Create new DOjo in Database
    @classmethod
    def new_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW());'

        return connectToMySQL('dojos_and_ninjas').query_db(query,data)







    # We need to import the burger class from our models

    @classmethod
    def show_ninja_from_dojo( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos = dojos.id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas').query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["ninjas.first_name"],
                "last_name" : row_from_db["ninjas.last_name"],
                "age" : row_from_db["ninjas.age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninja.append( ninja.Ninja( ninja_data ) )
        return dojo