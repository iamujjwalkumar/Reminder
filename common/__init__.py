import os, sys
path0 = os.getcwd()
currentf = os.path.basename(path0)
path = path0.replace('\\' + currentf, '')
sys.path.append(path)


from flask import Flask, request, jsonify, render_template, flash

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


import urllib.parse

load_dotenv()



TEMPLATE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "templates")
app = Flask(__name__, template_folder=TEMPLATE_DIR)

app.secret_key = "123" 


db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

database_uri = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

print(database_uri)


api = Api(app)

db = SQLAlchemy(app)


