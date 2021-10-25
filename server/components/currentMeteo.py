## getting data from db

import simplejson as json
from sqlalchemy import exc

def currentMeteo():
    from app import db, session
    print('currentMeteo')
    try:
        # SQL запросы
        session['sql_raw_meteo_now'] = 'select temp, clouds, wind_speed from forecast.his_data_openweathermap order by unix_dt desc limit 1'     
        session['sql_raw_meteo_now_2'] = 'select total_radiation from forecast.his_data_huawei where total_radiation is not null order by create_time desc limit 1'     
        
        #END --------- SQL запросы

        # Текущие метеоданные
        r = db.session.execute(session['sql_raw_meteo_now'])
        print('6')
        for row in r:
            print(row)
            
            if row['temp'] is None:
                session['currentTemp'] = 0   
                print('1')          
            else:
                session['currentTemp'] = json.dumps(row['temp'])  
                print('2')


            if row['clouds'] is None:
                session['currentClouds'] = 0             
            else:
                session['currentClouds'] = json.dumps(row['clouds'])

            if row['wind_speed'] is None:
                session['currentWind'] = 0             
            else:
                session['currentWind'] = json.dumps(row['wind_speed'])

        r = db.session.execute(session['sql_raw_meteo_now_2'])
        for row in r:
            
            if row['total_radiation'] is None:
                session['currentIrradiation'] = 0             
            else:
                session['currentIrradiation'] = json.dumps(row['total_radiation']) 

        # END ------ Текущие метеоданные


        session["result-now"] = 'done'
        return session["result-now"]

    except exc.SQLAlchemyError as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text