## getting data from db

import datetime
import simplejson as json


def getDB():
    from app import db, session, time, connection
    try:
        print('hehe ' + session.sid)
        start_time_getDB = time.time()
                
        his = []
        fc = []
        dt = []
        _sum = 0

        if "today" in session:
            print(session['today'])
            print("DBGET DATE --------------------------")
        else: 
            print('!!!!!!!!There was no session today var')
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
        cursor = connection.cursor()
        cursor.execute(session['sql_raw'])
        session['result'] = cursor.fetchall()
        print("WWS")
        print(session['result'][0][2])
        session['prognozfakt'] = json.dumps(session['result'][0][2])
        print("DBGET EXECUTE TIME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("--- %s seconds ---" % (time.time() - start_time_getDB))
        
        # session['result'] = db.session.execute(session['sql_raw'])
        # print("WWS")
        # print(session['result'])
        # print("DBGET EXECUTE TIME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print("--- %s seconds ---" % (time.time() - start_time_getDB))
        # session['prognozfakt'] = json.dumps(session['result'].first()[2])
        # print("DBGET DUMP TIME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print("--- %s seconds ---" % (time.time() - start_time_getDB))
        
        #END ----- Оправдываемость - значение

        # Метеоданные

        # r = db.session.execute(session['sql_raw_meteo_t'])
        cursor.execute(session['sql_raw_meteo_t'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

        session['meteo_t_graph_his'] = json.dumps(his)
        session['meteo_t_graph_fc'] = json.dumps(fc)
        print("DBGET DUMP LOOP TIME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("--- %s seconds ---" % (time.time() - start_time_getDB))

        # r = db.session.execute(session['sql_raw_meteo_c'])
        cursor.execute(session['sql_raw_meteo_c'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

        session['meteo_c_graph_his'] = json.dumps(his)
        session['meteo_c_graph_fc'] = json.dumps(fc)

        # r = db.session.execute(session['sql_raw_meteo_h'])
        cursor.execute(session['sql_raw_meteo_t'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

        session['meteo_h_graph_his'] = json.dumps(his)
        session['meteo_h_graph_fc'] = json.dumps(fc)

        # r = db.session.execute(session['sql_raw_meteo_w'])
        cursor.execute(session['sql_raw_meteo_w'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

        session['meteo_w_graph_his'] = json.dumps(his)
        session['meteo_w_graph_fc'] = json.dumps(fc)
        # END -------- Метеоданные

        # Оправдываемость
        # r = db.session.execute(session['sql_raw_2'])
        cursor.execute(session['sql_raw_2'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:            
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])
            
            if row[0] is None:
                dt.append(0)                
            else:
                dt.append(row[0])

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        session['prognozfakt_graph_dt'] = json.dumps(dt, default = myconverter)
        
        session['prognozfakt_graph_his'] = json.dumps(his)
        session['prognozfakt_graph_fc'] = json.dumps(fc)
        print("MOTHERFUCKER")
        # END ----- Оправдываемость

        # Текущая выработка
        # r = db.session.execute(session['sql_raw_today_2'])
        cursor.execute(session['sql_raw_today_2'])
        r = cursor.fetchall()
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:      
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])
            
            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

            
            if row[0] is None:
                dt.append(0)                
            else:
                dt.append(row[0])

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
        # r = db.session.execute(session['sql_raw_group'])
        cursor.execute(session['sql_raw_group'])
        r = cursor.fetchall()
        print(r)
        his.clear()
        fc.clear()
        dt.clear()

        for row in r:
            
            if row[1] is None:
                his.append(0)                
            else:
                his.append(row[1])

            if row[2] is None:
                fc.append(0)                
            else:
                fc.append(row[2])

        session['power_graph_his'] = json.dumps(his)
        session['power_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()

        # r = db.session.execute(session['sql_raw_group'])
        for row in r:            
            
            if row[6] is None:
                fc.append(0)                
            else:
                fc.append(row[6])
            
            if row[7] is None:
                his.append(0)                
            else:
                his.append(row[7])
            
        session['income_graph_his'] = json.dumps(his)
        session['income_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()
        
        # r = db.session.execute(session['sql_raw_group'])
        for row in r:            
        
            if row[8] is None:
                fc.append(0)                
            else:
                fc.append(row[8])

            if row[9] is None:
                his.append(0)                
            else:
                his.append(row[9])

        session['co2_graph_his'] = json.dumps(his)
        session['co2_graph_fc'] = json.dumps(fc)
        his.clear()
        fc.clear()

        # r = db.session.execute(session['sql_raw_group'])
        for row in r:            
        
            if row[4] is None:
                his.append(0)                
            else:
                his.append(row[4])
            
            if row[5] is None:
                fc.append(0)                
            else:
                fc.append(row[5])
                 
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