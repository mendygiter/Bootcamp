from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import user
from flask import flash
import re


class Recipe():

    def __init__(self, data):
        self.id = data['id']
        self.name= data['name']
        self.made_on = data['made_on']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data ['under_30_min']
        self.created_at = data ['created_at']
        self.updated_at = data['updated_at']

        self.users_id = data['users_id']

        self.posted_by = {}



    @classmethod
    def all_recipes(cls):

        query = 'SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;'

        results = connectToMySQL('recipe').query_db(query)

        recipes = []

        for row in results:
            print(row)
            recipe = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name' : row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row ['updated_at']

            }
            recipe.posted_by = user.User(user_data)
            recipes.append(recipe)
        return recipes


    #method to create new recipe
    @classmethod
    def new_recipe(self, data):
        query = 'INSERT INTO recipes (name, made_on, description, instructions, under_30_min, users_id) VALUES (%(name)s, %(made_on)s, %(description)s, %(instructions)s, %(under_30_min)s, %(user_id)s);'

        results = connectToMySQL('recipe').query_db(query, data)

        return results


    #method to view instructions
    @classmethod
    def get_one(cls,data):

        query = 'SELECT * FROM recipes WHERE id = %(id)s;'

        results = connectToMySQL('recipe').query_db(query, data)

        return cls(results[0])

    #edit recipe
    @classmethod
    def edit_recipe(cls,data):

        query = 'UPDATE recipes SET name = %(name)s, made_on = %(made_on)s, description = %(description)s, instructions = %(instructions)s, under_30_min = %(under_30_min)s WHERE id = %(id)s;'

        connectToMySQL('recipe').query_db(query, data)

    #delete recipe
    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'

        return connectToMySQL('recipe').query_db(query, data)



    #validating forms
    @staticmethod
    def validate_painting(data):

        is_valid = True

        if len(data['description']) < 3:
            is_valid = False
            flash('must be at least 3 characters long')

        if len(data['instructions']) < 3:
            is_valid = False
            flash('must be at least 3 characters long')

        if len(data['name']) < 3:
            is_valid = False
            flash('must be at least 3 characters long')

        if len(data['made_on']) != 10:
            is_valid = False
            flash('Please provide a date')
        
        return is_valid