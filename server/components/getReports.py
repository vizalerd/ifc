import simplejson as json
import datetime


def getReports():
    from app import db, session
    try:

        _id = []
        _date = []
        _target = []

        # SQL запросы
        session['sql_raw_reports'] = "select * from forecast.forecast_report_dates where forecast_date > date('" + session['today'] + "') "     
       
        #END --------- SQL запросы

        # 

        r = db.session.execute(session['sql_raw_reports'])
        for row in r:
            
            if row['id'] is None:
                _id.append(0)   
            else:
                _id.append(row['id'])  
                print(row['id'])

            if row['report_date'] is None:
                _date.append(0)   
            else:
                _date.append(row['report_date'].strftime(" %Y-%m-%d "))
                

            if row['forecast_date'] is None:
                _target.append(0)             
            else:
                 _target.append(row['forecast_date'].strftime(" %Y-%m-%d "))

     
        # END ------ Отчеты
        
        session['report_id'] = json.dumps(_id)
        session["report_date"] = json.dumps(_date)
        session["report_target"] = json.dumps(_target)
        return session["result-report"]

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text