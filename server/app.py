import sentry_sdk
from flask import Flask, jsonify, session, redirect, url_for
from sentry_sdk.integrations.flask import FlaskIntegration
from flask.globals import request
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import simplejson as json
from dotenv import load_dotenv
from decimal import Decimal
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, exc
import datetime
from flask_session import Session
import requests


load_dotenv()

# configuration
DEBUG = True

sentry_sdk.init(
    "https://facfff1886de4dd994e6359693967a5c@o1037880.ingest.sentry.io/6006012",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


# instantiate the app
app = Flask(__name__, static_folder='../dist/',    static_url_path='/')
app.config.from_object(__name__)

app.config['SECRET_KEY'] = "CtrhtnysqRk.x_2021"
app.config['SESSION_TYPE'] = 'filesystem'

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

sess = Session(app)



from components.currentMeteo import currentMeteo

# Set up the index route
@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    now = datetime.date.today()
    today = now - datetime.timedelta(days=1) 
    yesterday = today - datetime.timedelta(days=1) 

    session['date_start'] = yesterday.strftime("%Y-%m-%d")
    session['date_end'] = today.strftime("%Y-%m-%d")

    session['yesterday'] = yesterday.strftime("%Y-%m-%d")
    session['today'] = today.strftime("%Y-%m-%d")

    print(session.sid)
    return app.send_static_file('index.html')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

#import all vars


from components.dbGet import getDB

from components.dateRange import date_range

from components.getReports import getReports




# GET route
@app.route('/ping', methods=['GET'])
@cross_origin(supports_credentials=True)
def getRoute():
    try:
        getDB()
        print(session['prognozfakt'])
        return jsonify({ 'prognozfakt': session['prognozfakt'], 
                         'prognozfakt_graph_dt': session['prognozfakt_graph_dt'],
                         'prognozfakt_graph_fc': session['prognozfakt_graph_fc'],
                         'prognozfakt_graph_his': session['prognozfakt_graph_his'],
                         'today_prognozfakt': session['today_prognozfakt'], 
                         'today_prognozfakt_graph_dt': session['today_prognozfakt_graph_dt'],
                         'today_prognozfakt_graph_fc': session['today_prognozfakt_graph_fc'],
                         'today_prognozfakt_graph_his': session['today_prognozfakt_graph_his'],
                         'meteo_t_graph_his' : session['meteo_t_graph_his'],
                         'meteo_t_graph_fc' : session['meteo_t_graph_fc'],
                         'meteo_c_graph_his' : session['meteo_c_graph_his'],
                         'meteo_c_graph_fc' : session['meteo_c_graph_fc'],
                         'meteo_h_graph_his' : session['meteo_h_graph_his'],
                         'meteo_h_graph_fc' : session['meteo_h_graph_fc'],
                         'meteo_w_graph_his' : session['meteo_w_graph_his'],
                         'meteo_w_graph_fc' : session['meteo_w_graph_fc'],
                         'power_graph_his' : session['power_graph_his'],
                         'power_graph_fc' : session['power_graph_fc'],
                         'income_graph_his' : session['income_graph_his'],
                         'income_graph_fc' : session['income_graph_fc'],
                         'co2_graph_his' : session['co2_graph_his'],
                         'co2_graph_fc' : session['co2_graph_fc'],
                         'kium_graph_his' : session['kium_graph_his'],
                         'kium_graph_fc' : session['kium_graph_fc']
                        })
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

# POST route
@app.route('/ping', methods=['POST'])
@cross_origin(supports_credentials=True)
def postRoute():
    try:
        vo = request.json
        rd = date_range(vo)
        print('start = ' + rd['date_start'])
        print('end = ' + rd['date_end'])
        session['date_start'] = rd['date_start']
        session['date_end'] = rd['date_end']
        getDB()
        return jsonify({ 'prognozfakt': session['prognozfakt'], 
                         'prognozfakt_graph_dt': session['prognozfakt_graph_dt'],
                         'prognozfakt_graph_fc': session['prognozfakt_graph_fc'],
                         'prognozfakt_graph_his': session['prognozfakt_graph_his'],
                         'today_prognozfakt': session['today_prognozfakt'], 
                         'today_prognozfakt_graph_dt': session['today_prognozfakt_graph_dt'],
                         'today_prognozfakt_graph_fc': session['today_prognozfakt_graph_fc'],
                         'today_prognozfakt_graph_his': session['today_prognozfakt_graph_his'],
                         'meteo_t_graph_his' : session['meteo_t_graph_his'],
                         'meteo_t_graph_fc' : session['meteo_t_graph_fc'],
                         'meteo_c_graph_his' : session['meteo_c_graph_his'],
                         'meteo_c_graph_fc' : session['meteo_c_graph_fc'],
                         'meteo_h_graph_his' : session['meteo_h_graph_his'],
                         'meteo_h_graph_fc' : session['meteo_h_graph_fc'],
                         'meteo_w_graph_his' : session['meteo_w_graph_his'],
                         'meteo_w_graph_fc' : session['meteo_w_graph_fc'],
                         'power_graph_his' : session['power_graph_his'],
                         'power_graph_fc' : session['power_graph_fc'],
                         'income_graph_his' : session['income_graph_his'],
                         'income_graph_fc' : session['income_graph_fc'],
                         'co2_graph_his' : session['co2_graph_his'],
                         'co2_graph_fc' : session['co2_graph_fc'],
                         'kium_graph_his' : session['kium_graph_his'],
                         'kium_graph_fc' : session['kium_graph_fc']
                        }) 

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


from components.excelGenerate import excelGenerate

# EXCEL report
@app.route('/excel', methods=['GET'])
@cross_origin(supports_credentials=True)
def excelRoute():
    try:   
        excelGenerate()        
        return 'success'

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/drop")
@cross_origin(supports_credentials=True)
def logout():
    session.clear
    return redirect(url_for("index"))

@app.route("/getReports", methods=['GET'])
@cross_origin(supports_credentials=True)
def profile():
    getReports()
    return jsonify({ 'report_id' : session['report_id'],
                     'report_date' : session['report_date'],
                     'report_target' : session['report_target'],
    })

@app.route("/postReports", methods=['POST'])
@cross_origin(supports_credentials=True)
def profile_post():
    vo = request.json
    getReports()
    return jsonify({ 'report_id' : session['report_id'],
                     'report_date' : session['report_date'],
                     'report_target' : session['report_target'],
    })

@app.route('/currentMeteoInfo', methods=['GET'])
@cross_origin(supports_credentials=True)
def currentMet():
    currentMeteo()
    return jsonify({ 'currentTemp' : session['currentTemp'],
                     'currentClouds' : session['currentClouds'],
                     'currentWind' : session['currentWind'],
                     'currentIrradiation' : session['currentIrradiation'],
    })

if __name__ == '__main__':
    app.run()