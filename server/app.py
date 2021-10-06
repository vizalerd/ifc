from flask import Flask, jsonify
from flask.globals import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import simplejson as json
from dotenv import load_dotenv
from decimal import Decimal
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

load_dotenv()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder='../dist/',    static_url_path='/')
app.config.from_object(__name__)

# db connection
username = 'r_forecast'
password = 'Q1w2e3r$'
userpass = 'postgresql+psycopg2://' + username + ':' + password + '@'
server  = '95.56.236.114:55432'
dbname   = '/db_forecast'


# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

#import all vars
from components import settings as s


from components.dbGet import getDB

from components.dateRange import date_range

# GET route
@app.route('/ping', methods=['GET'])
def getRoute():
    try:
        r = getDB()
        print('ololo '+ r['prognozfakt'])
        return jsonify({ 'prognozfakt': r['prognozfakt'], 
                         'prognozfakt_graph_dt': r['prognozfakt_graph_dt'],
                         'prognozfakt_graph_fc': r['prognozfakt_graph_fc'],
                         'prognozfakt_graph_his': r['prognozfakt_graph_his'],
                         'today_prognozfakt': r['today_prognozfakt'], 
                         'today_prognozfakt_graph_dt': r['today_prognozfakt_graph_dt'],
                         'today_prognozfakt_graph_fc': r['today_prognozfakt_graph_fc'],
                         'today_prognozfakt_graph_his': r['today_prognozfakt_graph_his'],
                         'meteo_t_graph_his' : r['meteo_t_graph_his'],
                         'meteo_t_graph_fc' : r['meteo_t_graph_fc'],
                         'meteo_c_graph_his' : r['meteo_c_graph_his'],
                         'meteo_c_graph_fc' : r['meteo_c_graph_fc'],
                         'meteo_h_graph_his' : r['meteo_h_graph_his'],
                         'meteo_h_graph_fc' : r['meteo_h_graph_fc'],
                         'meteo_w_graph_his' : r['meteo_w_graph_his'],
                         'meteo_w_graph_fc' : r['meteo_w_graph_fc'],
                         'power_graph_his' : r['power_graph_his'],
                         'power_graph_fc' : r['power_graph_fc'],
                         'income_graph_his' : r['income_graph_his'],
                         'income_graph_fc' : r['income_graph_fc'],
                         'co2_graph_his' : r['co2_graph_his'],
                         'co2_graph_fc' : r['co2_graph_fc'],
                         'kium_graph_his' : r['kium_graph_his'],
                         'kium_graph_fc' : r['kium_graph_fc']
                        })
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

# POST route
@app.route('/ping', methods=['POST'])
def postRoute():
    try:
        vo = request.json
        r = date_range(vo)
        print('start = ' + r['date_start'])
        print('end = ' + r['date_end'])
        getDB()
        return {
            'date_start' : r['date_start'],
            'date_end' : r['date_end'],
        } 

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


from components.excelGenerate import excelGenerate

# EXCEL report
@app.route('/excel', methods=['GET'])
def excelRoute():
    try:   
        excelGenerate()        
        return 'success'

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run()