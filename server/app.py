from flask import Flask, jsonify, send_from_directory
from flask.globals import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from io import BytesIO
import psycopg2
import sqlalchemy
import simplejson as json
import array as arr
import datetime
from dotenv import load_dotenv
import os
from decimal import Decimal
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

load_dotenv()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder='../dist/',    static_url_path='/')
app.config.from_object(__name__)

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# db connection
username = 'r_forecast'
password = 'Q1w2e3r$'
userpass = 'postgresql+psycopg2://' + username + ':' + password + '@'
server  = '95.56.236.114:55432'
dbname   = '/db_forecast'


# change NOTHING below

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

prognozfakt_graph_his = []
prognozfakt_graph_fc = []
prognozfakt_graph_dt = []
meteo_t_graph_his = []
meteo_c_graph_his = []
meteo_h_graph_his = []
meteo_w_graph_his = []
meteo_t_graph_fc = []
meteo_c_graph_fc = []
meteo_h_graph_fc = []
meteo_w_graph_fc = []
now = datetime.date.today()
today = now - datetime.timedelta(days=1) 
yesterday = today - datetime.timedelta(days=1) 

g_date_start = yesterday.strftime("%Y-%m-%d")
g_date_end = today.strftime("%Y-%m-%d")

print('dadadad ' + yesterday.strftime("%Y-%m-%d"))

# get info from db
def getDB():
    try:
        
        prognozfakt_graph_his.clear()
        prognozfakt_graph_fc.clear()
        prognozfakt_graph_dt.clear()
        meteo_t_graph_his.clear()
        meteo_c_graph_his.clear()
        meteo_h_graph_his.clear()
        meteo_w_graph_his.clear()
        meteo_t_graph_fc.clear()
        meteo_c_graph_fc.clear()
        meteo_h_graph_fc.clear()
        meteo_w_graph_fc.clear()

        sql_raw = 'select * from "forecast"."get_rep_power"'+"('"+ g_date_start + "','"+ g_date_end +"')"
        sql_raw_2 = 'select * from "forecast"."get_rep_power_graph"'+"('"+ g_date_start + "','"+ g_date_end +"')"
        sql_raw_meteo_t = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ g_date_start + "','"+ g_date_end +"', 1)"
        sql_raw_meteo_c = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ g_date_start + "','"+ g_date_end +"', 2)"
        sql_raw_meteo_h = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ g_date_start + "','"+ g_date_end +"', 3)"
        sql_raw_meteo_w = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ g_date_start + "','"+ g_date_end +"', 4)"
        
        result = db.session.execute(sql_raw)
        prognozfakt = result.first()[2]
        d_json_prognozfakt = json.dumps(prognozfakt)

        result_meteo_t = db.session.execute(sql_raw_meteo_t)
        for row in result_meteo_t:
            
            if row['his'] is None:
                meteo_t_graph_his.append(0)                
            else:
                meteo_t_graph_his.append(row['his'])
            
            if row['fc'] is None:
                meteo_t_graph_fc.append(0)                
            else:
                meteo_t_graph_fc.append(row['fc'])

        d_json_meteo_t_graph_his = json.dumps(meteo_t_graph_his)
        d_json_meteo_t_graph_fc = json.dumps(meteo_t_graph_fc)

        result_meteo_c = db.session.execute(sql_raw_meteo_c)
        for row in result_meteo_c:
            
            if row['his'] is None:
                meteo_c_graph_his.append(0)                
            else:
                meteo_c_graph_his.append(row['his'])
            
            if row['fc'] is None:
                meteo_c_graph_fc.append(0)                
            else:
                meteo_c_graph_fc.append(row['fc'])

        d_json_meteo_c_graph_his = json.dumps(meteo_c_graph_his)
        d_json_meteo_c_graph_fc = json.dumps(meteo_c_graph_fc)

        result_meteo_h = db.session.execute(sql_raw_meteo_h)
        for row in result_meteo_h:
            
            if row['his'] is None:
                meteo_h_graph_his.append(0)                
            else:
                meteo_h_graph_his.append(row['his'])
            
            if row['fc'] is None:
                meteo_h_graph_fc.append(0)                
            else:
                meteo_h_graph_fc.append(row['fc'])

        d_json_meteo_h_graph_his = json.dumps(meteo_h_graph_his)
        d_json_meteo_h_graph_fc = json.dumps(meteo_h_graph_fc)

        result_meteo_w = db.session.execute(sql_raw_meteo_w)
        for row in result_meteo_w:
            
            if row['his'] is None:
                meteo_w_graph_his.append(0)                
            else:
                meteo_w_graph_his.append(row['his'])
            
            if row['fc'] is None:
                meteo_w_graph_fc.append(0)                
            else:
                meteo_w_graph_fc.append(row['fc'])

        d_json_meteo_w_graph_his = json.dumps(meteo_w_graph_his)
        d_json_meteo_w_graph_fc = json.dumps(meteo_w_graph_fc)




        result_2 = db.session.execute(sql_raw_2)

        for row in result_2:
            
            if row['his_power'] is None:
                prognozfakt_graph_his.append(0)                
            else:
                prognozfakt_graph_his.append(row['his_power'])
            
            if row['fc_power'] is None:
                prognozfakt_graph_fc.append(0)                
            else:
                prognozfakt_graph_fc.append(row['fc_power'])
            
            if row['dt'] is None:
                prognozfakt_graph_dt.append(0)                
            else:
                prognozfakt_graph_dt.append(row['dt'])

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        d_json_prognozfakt_graph_dt = json.dumps(prognozfakt_graph_dt, default = myconverter)
        
        d_json_prognozfakt_graph_fc = json.dumps(prognozfakt_graph_fc)
        d_json_prognozfakt_graph_his = json.dumps(prognozfakt_graph_his)
        print ("getDB done : ")
        
        return { 'prognozfakt': d_json_prognozfakt, 
                         'prognozfakt_graph_dt': d_json_prognozfakt_graph_dt,
                         'prognozfakt_graph_fc': d_json_prognozfakt_graph_fc,
                         'prognozfakt_graph_his': d_json_prognozfakt_graph_his,
                         'meteo_t_graph_his' : d_json_meteo_t_graph_his,
                         'meteo_t_graph_fc' : d_json_meteo_t_graph_fc,
                         'meteo_c_graph_his' : d_json_meteo_c_graph_his,
                         'meteo_c_graph_fc' : d_json_meteo_c_graph_fc,
                         'meteo_h_graph_his' : d_json_meteo_h_graph_his,
                         'meteo_h_graph_fc' : d_json_meteo_h_graph_fc,
                         'meteo_w_graph_his' : d_json_meteo_w_graph_his,
                         'meteo_w_graph_fc' : d_json_meteo_w_graph_fc,
                        }
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


#change date
def date_range(vo):
    try:
        global g_date_start
        global g_date_end
        g_date_start = vo[0][0:10]
        g_date_end = vo[1][0:10]
        return {
            'date_start' : g_date_start,
            'date_end' : g_date_end
        } 

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

# this route will test the database connection and nothing more
@app.route('/ping', methods=['GET'])
def getRoute():
    try:
        now = datetime.datetime.now()
        print ("Before date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        r = getDB()
        now = datetime.datetime.now()
        print ("After date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        return jsonify({ 'prognozfakt': r['prognozfakt'], 
                         'prognozfakt_graph_dt': r['prognozfakt_graph_dt'],
                         'prognozfakt_graph_fc': r['prognozfakt_graph_fc'],
                         'prognozfakt_graph_his': r['prognozfakt_graph_his'],
                         'meteo_t_graph_his' : r['meteo_t_graph_his'],
                         'meteo_t_graph_fc' : r['meteo_t_graph_fc'],
                         'meteo_c_graph_his' : r['meteo_c_graph_his'],
                         'meteo_c_graph_fc' : r['meteo_c_graph_fc'],
                         'meteo_h_graph_his' : r['meteo_h_graph_his'],
                         'meteo_h_graph_fc' : r['meteo_h_graph_fc'],
                         'meteo_w_graph_his' : r['meteo_w_graph_his'],
                         'meteo_w_graph_fc' : r['meteo_w_graph_fc'],
                        })
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/ping', methods=['POST'])
def postRoute():
    print('lol')
    try:
        vo = request.json
        r = date_range(vo)
        print(r['date_start'])
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

def download_file(report_name):
    try:
        print(report_name)
        return send_from_directory(directory=os.path.dirname(app.instance_path), 
                                    filename=report_name, 
                                    as_attachment=True)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

import xlsxwriter

@app.route('/excel', methods=['GET'])
def excelRoute():
    # keys = prognozfakt_graph_fc
    # values = prognozfakt_graph_his
    # dictionary = dict(zip(keys, values))
    print(prognozfakt_graph_his)
    try:
   
        now = datetime.datetime.now()
        report_name = 'iForecast-Отчет-' + now.strftime("%Y-%m-%d") + '.xlsx'
        with xlsxwriter.Workbook(report_name) as workbook:
            worksheet = workbook.add_worksheet()

            bold = workbook.add_format({'bold': 1})
            date_format = workbook.add_format({'num_format': 'm/d/yyyy h:mm'})
            worksheet.set_column(0, 3, 30)

            worksheet.write('A1', 'Время', bold)
            worksheet.write('B1', 'Прогноз', bold)
            worksheet.write('C1', 'Факт', bold)

            row = 1
            col = 0
            for date in (prognozfakt_graph_dt):
                worksheet.write_datetime(row, col, date, date_format )
                row += 1
            
            row = 1
            col = 1
            for fc in (prognozfakt_graph_fc):
                worksheet.write(row, col, fc)
                row += 1

            row = 1
            col = 2
            for his in (prognozfakt_graph_his):
                worksheet.write(row, col, his)
                row += 1

            # Write a total using a formula.
            worksheet.write(row, 0, 'Прогноз/Факт', bold)
            worksheet.write(row, 2, '=SUM(C2:C5)')


        
        return send_from_directory(directory=os.path.dirname(app.instance_path), 
                                    filename=report_name, 
                                    as_attachment=True)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(port=(os.getenv('PORT') if os.getenv('PORT') else 8000), debug=False)