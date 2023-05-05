"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaab33hp8u791gt6o20-a.oregon-postgres.render.com",
        database="todo_c8u8",
        user="root",
        password="D6y67Idmpe1jiDxw5BNnicdBniLfI83o")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
