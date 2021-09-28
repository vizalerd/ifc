import app

# get info from db
def get_db():
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
