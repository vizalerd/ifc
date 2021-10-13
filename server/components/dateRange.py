#change date
import datetime

def date_range(vo):
    try:
        print('vo = ' + vo[0])
        date_start = datetime.datetime.strptime(vo[0][0:10], "%Y-%m-%d")
        date_start =  date_start + datetime.timedelta(days=1)
        date_start =  date_start.strftime("%Y-%m-%d")
        date_end = datetime.datetime.strptime(vo[1][0:10], "%Y-%m-%d")
        date_end =  date_end + datetime.timedelta(days=2)
        date_end =  date_end.strftime("%Y-%m-%d")
        return {
            'date_start' : date_start,
            'date_end' : date_end
        } 

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        print(hed + error_text)
        return hed + error_text