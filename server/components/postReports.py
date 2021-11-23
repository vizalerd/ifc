import simplejson as json
import datetime


def postReports(vo):
    from app import db, session
    try:

        print('post report')
        print(vo[0:10])

        # SQL запросы
        session['sql_raw_reports_post'] = "insert into forecast.forecast_report_dates (report_date, forecast_date) values (date('" + session['today'] + "'), date('" + vo[0:10] + "'))"     
        print(session['sql_raw_reports_post'])
        #END --------- SQL запросы

        # 

        
        
        r = db.session.execute(session['sql_raw_reports_post'])
        
        return 'success'

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text