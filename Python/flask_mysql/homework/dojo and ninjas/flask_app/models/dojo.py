from  flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def all_dojos(cls):
        query = 'SELECT * FROM dojo_and_ninjas;'

        results = connectToMySQL('dojos').query.db(query)

        dojos = []

        for row in results:
            dojos.append(cls(row))
        return dojos