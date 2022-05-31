from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import user
from flask import flash
import re


class Painting():

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data ['price']
        self.created_at = data ['created_at']
        self.updated_at = data['updated_at']

        self.users_id = data['users_id']

        self.made_by = {}


    @classmethod
    def all_paintings(cls):

        query = 'SELECT * FROM paintings JOIN users ON paintings.users_id = users.id;'

        results = connectToMySQL('artist').query_db(query)

        paintings = []

        for row in results:
            print(row)
            painting = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name' : row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row ['updated_at']

            }
            painting.made_by = user.User(user_data)
            paintings.append(painting)
        return paintings


    #method to create new recipe
    @classmethod
    def new_painting(self, data):
        query = 'INSERT INTO paintings (title, description, price, users_id) VALUES (%(title)s, %(description)s, %(price)s, %(users_id)s);'

        results = connectToMySQL('artist').query_db(query, data)

        return results


    @classmethod
    def get_one(cls,data):

        query = 'SELECT * FROM paintings WHERE id = %(id)s;'

        results = connectToMySQL('artist').query_db(query, data)

        return cls(results[0])


    #edit recipe
    @classmethod
    def edit_painting(cls,data):

        query = 'UPDATE paintings SET title = %(title)s,  description = %(description)s, price = %(price)s, users_id = %(user_id)s WHERE id = %(id)s;'

        connectToMySQL('artist').query_db(query, data)


    #delete recipe
    @classmethod
    def delete_painting(cls, data):
        query = 'DELETE FROM paintings WHERE id = %(id)s;'

        return connectToMySQL('artist').query_db(query, data)



        #validating forms
    @staticmethod
    def validate_painting(data):

        is_valid = True

        if len(data['title']) < 2:
            is_valid = False
            flash('title must be at least 3 characters long')

        if len(data['description']) < 10:
            is_valid = False
            flash('description must be at least 3 characters long')

        if len(data['price']) < 0:
            is_valid = False
            flash('price must be at least 3 characters long')

        # if len(data['made_on']) != 10:
        #     is_valid = False
        #     flash('Please provide a date')
        
        return is_valid