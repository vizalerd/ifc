import datetime

global g_date_start
global g_date_end
global g_date_today
global g_date_yesterday

#Оправдываемость
prognozfakt = ''

#Прогноз/Факт
prognozfakt_graph_his = []
prognozfakt_graph_fc = []

#Временной промежуток
prognozfakt_graph_dt = []


#Оправдываемость ----- /Текущая
today_prognozfakt = ''

#Прогноз/Факт ----- /Текущая
today_prognozfakt_graph_his = []
today_prognozfakt_graph_fc = []

#Временной промежуток ----- /Текущая
today_prognozfakt_graph_dt = []

#Погода
meteo_t_graph_his = []
meteo_c_graph_his = []
meteo_h_graph_his = []
meteo_w_graph_his = []
meteo_t_graph_fc = []
meteo_c_graph_fc = []
meteo_h_graph_fc = []
meteo_w_graph_fc = []

#Общая выработка
power_graph_his = []
power_graph_fc = []

#Доход
income_graph_his = []
income_graph_fc = []

#Выбросы
co2_graph_his = []
co2_graph_fc = []

#КИУМ
kium_graph_his = []
kium_graph_fc = []


now = datetime.date.today()
today = now - datetime.timedelta(days=1) 
yesterday = today - datetime.timedelta(days=1) 

g_date_start = yesterday.strftime("%Y-%m-%d")
g_date_end = today.strftime("%Y-%m-%d")

g_date_yesterday = yesterday.strftime("%Y-%m-%d")
g_date_today = today.strftime("%Y-%m-%d")
