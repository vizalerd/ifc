## getting data from db

from components import settings as s
import datetime
import simplejson as json


def getDB():
    from app import db, session
    try:
        
        his = []
        fc = []
        dt = []
        _sum = 0
        print(session['date_start'] + ' !!!! ' + session['date_end'])

        # SQL запросы
        session['sql_raw'] = 'select * from "forecast"."get_rep_power"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"')"
        # sql_raw_today = 'select * from "forecast"."get_rep_power"'+"('"+ s.g_date_yesterday + "','"+ s.g_date_today +"')"
        session['sql_raw_2'] = 'select * from "forecast"."get_rep_power_graph"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"')"
        session['sql_raw_today_2'] = 'select * from "forecast"."get_rep_power_graph"'+"('"+ session['yesterday'] + "','"+ session['today'] +"')"
        session['sql_raw_meteo_t'] = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"', 1)"
        session['sql_raw_meteo_c'] = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"', 2)"
        session['sql_raw_meteo_h'] = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"', 3)"
        session['sql_raw_meteo_w'] = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"', 4)"
        session['sql_raw_group'] = 'select * from "forecast"."get_rep_kuim"'+"('"+ session['date_start'] + "','"+ session['date_end'] +"')"      
        #END --------- SQL запросы

        # Оправдываемость - значение  
        session['result'] = db.session.execute(session['sql_raw'])
        session['prognozfakt'] = json.dumps(session['result'].first()[2])
        #END ----- Оправдываемость - значение

        # Метеоданные
        r = db.session.execute(session['sql_raw_meteo_t'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row['his'] is None:
                his.append(0)                
            else:
                his.append(row['his'])
            
            if row['fc'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc'])

        session['meteo_t_graph_his'] = json.dumps(his)
        session['meteo_t_graph_fc'] = json.dumps(fc)

        r = db.session.execute(session['sql_raw_meteo_c'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row['his'] is None:
                his.append(0)                
            else:
                his.append(row['his'])
            
            if row['fc'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc'])

        session['meteo_c_graph_his'] = json.dumps(his)
        session['meteo_c_graph_fc'] = json.dumps(fc)

        r = db.session.execute(session['sql_raw_meteo_h'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row['his'] is None:
                his.append(0)                
            else:
                his.append(row['his'])
            
            if row['fc'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc'])

        session['meteo_h_graph_his'] = json.dumps(his)
        session['meteo_h_graph_fc'] = json.dumps(fc)

        r = db.session.execute(session['sql_raw_meteo_w'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row['his'] is None:
                his.append(0)                
            else:
                his.append(row['his'])
            
            if row['fc'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc'])

        session['meteo_w_graph_his'] = json.dumps(his)
        session['meteo_w_graph_fc'] = json.dumps(fc)
        # END -------- Метеоданные

        # Оправдываемость
        r = db.session.execute(session['sql_raw_2'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:            
            
            if row['his_power'] is None:
                his.append(0)                
            else:
                his.append(row['his_power'])
            
            if row['fc_power'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_power'])
            
            if row['dt'] is None:
                dt.append(0)                
            else:
                dt.append(row['dt'])

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        session['prognozfakt_graph_dt'] = json.dumps(dt, default = myconverter)
        
        session['prognozfakt_graph_his'] = json.dumps(his)
        session['prognozfakt_graph_fc'] = json.dumps(fc)
        # END ----- Оправдываемость

        # Текущая выработка
        r = db.session.execute(session['sql_raw_today_2'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:      
            if row['his_power'] is None:
                his.append(0)                
            else:
                his.append(row['his_power'])
            
            if row['fc_power'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_power'])

            
            if row['dt'] is None:
                dt.append(0)                
            else:
                dt.append(row['dt'])

        _sum = sum(his)

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        session['today_prognozfakt_graph_dt'] = json.dumps(dt, default = myconverter)
        
        session['today_prognozfakt_graph_fc'] = json.dumps(fc)
        session['today_prognozfakt_graph_his'] = json.dumps(his)
        session['today_prognozfakt'] = json.dumps(_sum)        
        # END ----- Текущая выработка


        # Общая выработка, Доход, СО2, КУИМ
        r = db.session.execute(session['sql_raw_group'])
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row['his_power'] is None:
                his.append(0)                
            else:
                his.append(row['his_power'])

            if row['fc_power'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_power'])

        session['power_graph_his'] = json.dumps(his)
        session['power_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()

        r = db.session.execute(session['sql_raw_group'])
        for row in r:            
            
            if row['fc_income'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_income'])
            
            if row['his_income'] is None:
                his.append(0)                
            else:
                his.append(row['his_income'])
            
        session['income_graph_his'] = json.dumps(his)
        session['income_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()
        
        r = db.session.execute(session['sql_raw_group'])
        for row in r:            
        
            if row['fc_co2'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_co2'])

            if row['his_co2'] is None:
                his.append(0)                
            else:
                his.append(row['his_co2'])

        session['co2_graph_his'] = json.dumps(his)
        session['co2_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()

        r = db.session.execute(session['sql_raw_group'])
        for row in r:            
        
            if row['his_kuim'] is None:
                his.append(0)                
            else:
                his.append(row['his_kuim'])
            
            if row['fc_kuim'] is None:
                fc.append(0)                
            else:
                fc.append(row['fc_kuim'])
                 
        session['kium_graph_his'] = json.dumps(his)
        session['kium_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()
        # END ----- Общая выработка, Доход, СО2, КУИМ


        session["result"] = 'done'
        return session["result"]

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text