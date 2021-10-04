## getting data from db

from components import settings as s
import datetime
import simplejson as json


def getDB():
    from app import db
    try:
        
        s.prognozfakt_graph_his.clear()
        s.prognozfakt_graph_fc.clear()
        s.prognozfakt_graph_dt.clear()
        s.today_prognozfakt_graph_his.clear()
        s.today_prognozfakt_graph_fc.clear()
        s.today_prognozfakt_graph_dt.clear()
        s.meteo_t_graph_his.clear()
        s.meteo_c_graph_his.clear()
        s.meteo_h_graph_his.clear()
        s.meteo_w_graph_his.clear()
        s.meteo_t_graph_fc.clear()
        s.meteo_c_graph_fc.clear()
        s.meteo_h_graph_fc.clear()
        s.meteo_w_graph_fc.clear()
        s.power_graph_his.clear()
        s.power_graph_fc.clear()
        s.income_graph_his.clear()
        s.income_graph_fc.clear()
        s.co2_graph_his.clear()
        s.co2_graph_fc.clear()
        s.kium_graph_his.clear()
        s.kium_graph_fc.clear()

        print(s.g_date_start + ' !!!! ' + s.g_date_end)

        # SQL запросы
        sql_raw = 'select * from "forecast"."get_rep_power"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"')"
        # sql_raw_today = 'select * from "forecast"."get_rep_power"'+"('"+ s.g_date_yesterday + "','"+ s.g_date_today +"')"
        sql_raw_2 = 'select * from "forecast"."get_rep_power_graph"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"')"
        sql_raw_today_2 = 'select * from "forecast"."get_rep_power_graph"'+"('"+ s.g_date_yesterday + "','"+ s.g_date_today +"')"
        sql_raw_meteo_t = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"', 1)"
        sql_raw_meteo_c = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"', 2)"
        sql_raw_meteo_h = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"', 3)"
        sql_raw_meteo_w = 'select * from "forecast"."get_rep_meteo_graph"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"', 4)"
        sql_raw_group = 'select * from "forecast"."get_rep_kuim"'+"('"+ s.g_date_start + "','"+ s.g_date_end +"')"      
        #END --------- SQL запросы

        # Оправдываемость - значение  
        result = db.session.execute(sql_raw)
        prognozfakt = result.first()[2]
        d_json_prognozfakt = json.dumps(prognozfakt)
        #END ----- Оправдываемость - значение

        # Метеоданные
        result_meteo_t = db.session.execute(sql_raw_meteo_t)
        for row in result_meteo_t:
            
            if row['his'] is None:
                s.meteo_t_graph_his.append(0)                
            else:
                s.meteo_t_graph_his.append(row['his'])
            
            if row['fc'] is None:
                s.meteo_t_graph_fc.append(0)                
            else:
                s.meteo_t_graph_fc.append(row['fc'])

        d_json_meteo_t_graph_his = json.dumps(s.meteo_t_graph_his)
        d_json_meteo_t_graph_fc = json.dumps(s.meteo_t_graph_fc)

        result_meteo_c = db.session.execute(sql_raw_meteo_c)
        for row in result_meteo_c:
            
            if row['his'] is None:
                s.meteo_c_graph_his.append(0)                
            else:
                s.meteo_c_graph_his.append(row['his'])
            
            if row['fc'] is None:
                s.meteo_c_graph_fc.append(0)                
            else:
                s.meteo_c_graph_fc.append(row['fc'])

        d_json_meteo_c_graph_his = json.dumps(s.meteo_c_graph_his)
        d_json_meteo_c_graph_fc = json.dumps(s.meteo_c_graph_fc)

        result_meteo_h = db.session.execute(sql_raw_meteo_h)
        for row in result_meteo_h:
            
            if row['his'] is None:
                s.meteo_h_graph_his.append(0)                
            else:
                s.meteo_h_graph_his.append(row['his'])
            
            if row['fc'] is None:
                s.meteo_h_graph_fc.append(0)                
            else:
                s.meteo_h_graph_fc.append(row['fc'])

        d_json_meteo_h_graph_his = json.dumps(s.meteo_h_graph_his)
        d_json_meteo_h_graph_fc = json.dumps(s.meteo_h_graph_fc)

        result_meteo_w = db.session.execute(sql_raw_meteo_w)
        for row in result_meteo_w:
            
            if row['his'] is None:
                s.meteo_w_graph_his.append(0)                
            else:
                s.meteo_w_graph_his.append(row['his'])
            
            if row['fc'] is None:
                s.meteo_w_graph_fc.append(0)                
            else:
                s.meteo_w_graph_fc.append(row['fc'])

        d_json_meteo_w_graph_his = json.dumps(s.meteo_w_graph_his)
        d_json_meteo_w_graph_fc = json.dumps(s.meteo_w_graph_fc)
        # END -------- Метеоданные

        # Оправдываемость
        result_2 = db.session.execute(sql_raw_2)

        for row in result_2:            
            
            if row['his_power'] is None:
                s.prognozfakt_graph_his.append(0)                
            else:
                s.prognozfakt_graph_his.append(row['his_power'])
            
            if row['fc_power'] is None:
                s.prognozfakt_graph_fc.append(0)                
            else:
                s.prognozfakt_graph_fc.append(row['fc_power'])
            
            if row['dt'] is None:
                s.prognozfakt_graph_dt.append(0)                
            else:
                s.prognozfakt_graph_dt.append(row['dt'])

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        d_json_prognozfakt_graph_dt = json.dumps(s.prognozfakt_graph_dt, default = myconverter)
        
        d_json_prognozfakt_graph_fc = json.dumps(s.prognozfakt_graph_fc)
        d_json_prognozfakt_graph_his = json.dumps(s.prognozfakt_graph_his)
        # END ----- Оправдываемость

        # Текущая выработка
        result_today_2 = db.session.execute(sql_raw_today_2)

        for row in result_today_2:      
            if row['his_power'] is None:
                s.today_prognozfakt_graph_his.append(0)                
            else:
                s.today_prognozfakt_graph_his.append(row['his_power'])
            
            if row['fc_power'] is None:
                s.today_prognozfakt_graph_fc.append(0)                
            else:
                s.today_prognozfakt_graph_fc.append(row['fc_power'])

            
            if row['dt'] is None:
                s.today_prognozfakt_graph_dt.append(0)                
            else:
                s.today_prognozfakt_graph_dt.append(row['dt'])

        today_prognozfakt = sum(s.today_prognozfakt_graph_his)

        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        d_json_prognozfakt_graph_dt_today = json.dumps(s.today_prognozfakt_graph_dt, default = myconverter)
        
        d_json_prognozfakt_graph_fc_today = json.dumps(s.today_prognozfakt_graph_fc)
        d_json_prognozfakt_graph_his_today = json.dumps(s.today_prognozfakt_graph_his)
        d_json_prognozfakt_today = json.dumps(today_prognozfakt)        
        # END ----- Текущая выработка


        # Общая выработка, Доход, СО2, КУИМ
        result_group = db.session.execute(sql_raw_group)

        for row in result_group:
            
            if row['his_power'] is None:
                s.power_graph_his.append(0)                
            else:
                s.power_graph_his.append(row['his_power'])
            
            if row['fc_power'] is None:
                s.power_graph_fc.append(0)                
            else:
                s.power_graph_fc.append(row['fc_power'])
            
            if row['fc_income'] is None:
                s.income_graph_fc.append(0)                
            else:
                s.income_graph_fc.append(row['fc_income'])
            
            if row['his_income'] is None:
                s.income_graph_his.append(0)                
            else:
                s.income_graph_his.append(row['his_income'])
            
            if row['fc_co2'] is None:
                s.co2_graph_fc.append(0)                
            else:
                s.co2_graph_fc.append(row['fc_co2'])

            if row['his_co2'] is None:
                s.co2_graph_his.append(0)                
            else:
                s.co2_graph_his.append(row['his_co2'])

            if row['his_kuim'] is None:
                s.kium_graph_his.append(0)                
            else:
                s.kium_graph_his.append(row['his_kuim'])
            
            if row['fc_kuim'] is None:
                s.kium_graph_fc.append(0)                
            else:
                s.kium_graph_fc.append(row['fc_kuim'])
                

        d_json_power_graph_his = json.dumps(s.power_graph_his)
        d_json_power_graph_fc = json.dumps(s.power_graph_fc)
        d_json_income_graph_his = json.dumps(s.income_graph_his)
        d_json_income_graph_fc = json.dumps(s.income_graph_fc)
        d_json_co2_graph_his = json.dumps(s.co2_graph_his)
        d_json_co2_graph_fc = json.dumps(s.co2_graph_fc)
        d_json_kium_graph_his = json.dumps(s.kium_graph_his)
        d_json_kium_graph_fc = json.dumps(s.kium_graph_fc)
        # END ----- Общая выработка, Доход, СО2, КУИМ


        


        print ("getDB done : ")
        
        return {    'prognozfakt': d_json_prognozfakt, 
                    'prognozfakt_graph_dt': d_json_prognozfakt_graph_dt,
                    'prognozfakt_graph_fc': d_json_prognozfakt_graph_fc,
                    'prognozfakt_graph_his': d_json_prognozfakt_graph_his,
                    'today_prognozfakt': d_json_prognozfakt_today, 
                    'today_prognozfakt_graph_dt': d_json_prognozfakt_graph_dt_today,
                    'today_prognozfakt_graph_fc': d_json_prognozfakt_graph_fc_today,
                    'today_prognozfakt_graph_his': d_json_prognozfakt_graph_his_today,
                    'meteo_t_graph_his' : d_json_meteo_t_graph_his,
                    'meteo_t_graph_fc' : d_json_meteo_t_graph_fc,
                    'meteo_c_graph_his' : d_json_meteo_c_graph_his,
                    'meteo_c_graph_fc' : d_json_meteo_c_graph_fc,
                    'meteo_h_graph_his' : d_json_meteo_h_graph_his,
                    'meteo_h_graph_fc' : d_json_meteo_h_graph_fc,
                    'meteo_w_graph_his' : d_json_meteo_w_graph_his,
                    'meteo_w_graph_fc' : d_json_meteo_w_graph_fc,
                    'power_graph_his' : d_json_power_graph_his,
                    'power_graph_fc' : d_json_power_graph_fc,
                    'income_graph_his' : d_json_income_graph_his,
                    'income_graph_fc' : d_json_income_graph_fc,
                    'co2_graph_his' : d_json_co2_graph_his,
                    'co2_graph_fc' : d_json_co2_graph_fc,
                    'kium_graph_his' : d_json_kium_graph_his,
                    'kium_graph_fc' : d_json_kium_graph_fc
                }
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text