from unittest import result
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
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



    @classmethod
    def all_recipes(cls):

        query = 'SELECT * FROM recipes;'

        results = connectToMySQL('recipe').query_db(query)

        recipes = []

        for row in results:
            recipes.append(cls(row))
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
    def validate_recipe(data):

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

        if len(data['made_on']) < 3:
            is_valid = False
            flash('must be at least 3 characters long')
        