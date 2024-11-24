import sys
import os
import psycopg2
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

import routes

load_dotenv()

try:
    db_conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
except Exception as ex:
    print('Ошибка базы данных:', repr(ex))
    sys.exit()


app = Flask(__name__)

CORS(app)
app.config["WTF_CSRF_ENABLED"] = False

routes.init(app, db_conn)

if __name__ == '__main__':
    app.run(debug=True)