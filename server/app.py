import sentry_sdk
from flask import Flask, jsonify, session, redirect, url_for, flash, send_from_directory
import os
from os import environ

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
from werkzeug.security import generate_password_hash, check_password_hash


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

# app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')


app.config["REPORTS"] = os.path.dirname(app.instance_path) + "\_reports"

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

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Set up the index route
@app.route('/')
@cross_origin(supports_credentials=True)
def index():
    now = datetime.date.today()
    today = now 
    yesterday = today - datetime.timedelta(days=1) 

    print('now')
    print(today)

    session['date_start'] = yesterday.strftime("%Y-%m-%d")
    session['date_end'] = today.strftime("%Y-%m-%d")

    session['yesterday'] = yesterday.strftime("%Y-%m-%d")
    session['today'] = today.strftime("%Y-%m-%d")

    print('session[today]')
    print(session['today'])
    print('---------------------------------------')


    print(session.sid)
    
    
    return app.send_static_file('index.html')




class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

#import all vars


from components.dbGet import getDB

from components.dateRange import date_range

from components.getReports import getReports
from components.postReports import postReports


@app.route('/dashboard')
@cross_origin(supports_credentials=True)
def dashboard():
    return redirect('/#/dashboard')

@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    lol = 'lol'
    vo = request.json
    print('login')
    print(vo)
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        username = vo['username']
        password = vo['password']
        print(password)
 
        # Check if account exists using MySQL
        session['sql_raw_login'] = 'select * from forecast.users WHERE users.login = '+"'"+ username + "'"
        
        # Fetch one record and return result
        accounts = db.session.execute(session['sql_raw_login'])
 
        for account in accounts:
            password_rs = account['passw']
            print('ebat')
            print(password_rs)
            # If account exists in users table in out database
            # if check_password_hash(password_rs, password):
            if (password == password_rs):
                print('EQUAL')
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['login']
                # Redirect to home page
                r = "True"
                return jsonify({ 'isOK': json.dumps(r) })
            else:
                print("NOT EQUAL")
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password')
                r = "False"
                return jsonify({ 'isOK': json.dumps(r) })
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
 
    return redirect(url_for('index'))

@app.route('/isok', methods=['GET'])
def isOK():
    if 'loggedin' in session:
        return jsonify({ 'isOK': session['loggedin'] })
    else: 
        r = "false"
        return jsonify({ 'isOK': r })


# GET route
@app.route('/ping', methods=['GET'])
@cross_origin(supports_credentials=True)
def getRoute():
    try:
        print("ping current session")
        print(session.sid)
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
        print("report_name")

        session['report_name'] = "_" + excelGenerate()     
        print(session['report_name'])   
        return send_from_directory(app.config["REPORTS"], 
                                    filename=session['report_name'], 
                                    as_attachment=True)

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

@app.route("/getreports", methods=['GET'])
@cross_origin(supports_credentials=True)
def profile():
    getReports()
    return jsonify({ 'report_id' : session['report_id'],
                     'report_date' : session['report_date'],
                     'report_target' : session['report_target'],
    })

@app.route("/postreports", methods=['POST'])
@cross_origin(supports_credentials=True)
def profile_post():
    vo = request.json
    postReports(vo)
    return 'success'

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