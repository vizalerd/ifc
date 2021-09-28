import app

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
