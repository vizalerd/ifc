import datetime
import xlsxwriter
from flask import send_from_directory
import os
import random
import string
import simplejson as json


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def excelGenerate():
    from app import app, session

    try:
   
        now = datetime.datetime.now()
        session['report_name'] = 'iForecast-Отчет-' + now.strftime("%Y-%m-%d") + '#' + get_random_string(8) + '.xlsx'
        print("function report name")
        print(session['report_name'])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        full_report_name = os.path.dirname(app.instance_path) + "\_reports\_" + session['report_name']
        with xlsxwriter.Workbook(full_report_name) as workbook:
            worksheet = workbook.add_worksheet()
            print(session['report_name'])

            bold = workbook.add_format({'bold': 1})
            date_format = workbook.add_format({'num_format': 'm/d/yyyy h:mm:ss'})
            worksheet.set_column(0, 3, 30)

            worksheet.write('A1', 'Время', bold)
            worksheet.write('B1', 'Прогноз', bold)
            worksheet.write('C1', 'Факт', bold)


            
            
            row = 1
            col = 1
            excel_data = json.loads(session['prognozfakt_graph_fc'])
            for fc in (excel_data):
                worksheet.write(row, col, fc)
                row += 1

            row = 1
            col = 2
            excel_data = json.loads(session['prognozfakt_graph_his'])
            for his in (excel_data):
                worksheet.write(row, col, his)
                row += 1

            row = 1
            col = 0
            excel_data = json.loads(session['prognozfakt_graph_dt'])
            for date in (excel_data):
                date_time = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                worksheet.write_datetime(row, col, date_time, date_format )
                row += 1

            # Write a total using a formula.
            worksheet.write(row, 0, 'Прогноз/Факт', bold)
            worksheet.write(row, 2, session['prognozfakt'])

        
        return session['report_name']

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text