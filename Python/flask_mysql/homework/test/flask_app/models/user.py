from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
import re

class User():

    def __init__(self, data):
        self.id = data ['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']
        self.password = data ['password']
        self.created_at = data ['created_at']
        self.updated_at = data['updated_at']

    #method to add new user
    @classmethod
    def create_user(self, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'

        result = connectToMySQL('artist').query_db(query, data)

        return result

    #method to make sure no duplicate account with the same email
    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'

        results = connectToMySQL('artist').query_db(query, data)

        users = []

        for item in results:
            users.append(User(item))
        
        return users


    #method to make sure duplicates are not created
    @staticmethod
    def validate_user(data):

    #we always assume our data is valid to start with
        is_valid = True

        #Set email rules
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

            #first name must be valid length
        if len(data['first_name']) < 2:
            is_valid = False
            flash('First name must be at leat 2 characters')

            #last name must be valid length
        if len(data['last_name']) < 2:
            is_valid = False
            flash('Username must be at leat 2 characters')

    #email must follow a pattern
        if not email_regex.match(data['email']):
            is_valid = False
            flash('Please provide a valid email')

    #password must be at least 8 char
        if len(data['password']) < 10 or len(data['password']) > 60:
            is_valid = False
            flash('Password must be at least 10 char or maximum 60 char')

    #password and confirm password fields must match
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('Password and confirm password must match')

        return is_valid





























    # @classmethod
    # def get_user_by_email(cls, data):
    #     query = 'SELECT * FROM users WHERE email = %(email)s;'

    #     results = connectToMySQL('artist').query_db(query, data)

    #     users = []

    #     for item in results:
    #         users.append(User(item))
        
    #     return users


    #     #method to make sure no duplicate account with the same email
    # @classmethod
    # def get_user_by_email(cls, data):
    #     query = 'SELECT * FROM users WHERE email = %(email)s;'

    #     results = connectToMySQL('artist').query_db(query, data)

    #     users = []

    #     for item in results:
    #         users.append(User(item))
        
    #     return users


    # @staticmethod
    # def validate_user(data):

    # #we always assume our data is valid to start with
    #     is_valid = True
    #     email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

    # #username must be valid length
    #     if len(data['username']) < 3 or len(data['username']) > 20:
    #         is_valid = False
    #         flash('Username must be at leat 3 character, and up to 20')

    # # username must be uniqe
    #     if len(User.get_user_by_username(data))!= 0:
    #         is_valid = False 
    #         flash('Username already in use')



    # #email must follow a pattern
    #     if not email_regex.match(data['email']):
    #         is_valid = False
    #         flash('Please provide a valid email')



    # #email must be uniqe
    #     if len(User.get_user_by_email(data))!= 0:
    #         is_valid = False 
    #         flash('email already in use')



    # #password must be at least 8 char
    #     if len(data['password']) < 8 or len(data['password']) > 60:
    #         is_valid = False
    #         flash('Password must be at least 8 char or maximum 60 char')



    # #password and confirm password fields must match
    #     if data['password'] != data['confirm_password']:
    #         is_valid = False
    #         flash('Password and confirm password must match')

    #     return is_valid



    #     # ({'username': data['username']})) 