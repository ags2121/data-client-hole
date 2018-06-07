from flask import Flask
import psycopg2
import yaml

app = Flask(__name__)

creds = yaml.load(open('./creds.yaml'))

dbconn = psycopg2.connect(
    dbname=creds['d'], user=creds['u'], password=creds['p'], host=creds['h'])

@app.route("/client_data")
def client_data():
    return ""
