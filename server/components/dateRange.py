#change date
from components import settings as s

def date_range(vo):
    try:
        s.g_date_start = vo[0][0:10]
        s.g_date_end = vo[1][0:10]
        return {
            'date_start' : s.g_date_start,
            'date_end' : s.g_date_end
        } 

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text