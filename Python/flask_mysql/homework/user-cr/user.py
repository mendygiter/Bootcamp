from mysqlconnection import connectToMySQL
#1. we create the user class that is modeled after our erd in SQL-workbench
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
#2. create our method that will run our SQL querys and have the data shown on our site
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        # make sure to call the connectToMySQL function with the schema you are targeting.
        Results = connectToMySQL('users_cr').query_db(query)

        users = []

        for row in Results:
            users.append( cls(row) )
        return users


    @classmethod
    def new_user(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, created_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, NOW() );"

        return connectToMySQL('users_cr').query_db(query, data)
        
