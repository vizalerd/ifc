import datetime
import xlsxwriter
from flask import send_from_directory
import os
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def excelGenerate():
    from app import app, session

    try:
   
        now = datetime.datetime.now()
        report_name = os.path.dirname(app.instance_path) + '\_reports\iForecast-Отчет-' + now.strftime("%Y-%m-%d") + ' #' + get_random_string(8) + '.xlsx'
        with xlsxwriter.Workbook(report_name) as workbook:
            worksheet = workbook.add_worksheet()
            print(report_name)

            bold = workbook.add_format({'bold': 1})
            date_format = workbook.add_format({'num_format': 'm/d/yyyy h:mm'})
            worksheet.set_column(0, 3, 30)

            worksheet.write('A1', 'Время', bold)
            worksheet.write('B1', 'Прогноз', bold)
            worksheet.write('C1', 'Факт', bold)


            row = 1
            col = 0
            for date in (session['prognozfakt_graph_dt']):
                worksheet.write_datetime(row, col, date, date_format )
                row += 1
            
            row = 1
            col = 1
            for fc in (session['prognozfakt_graph_fc']):
                worksheet.write(row, col, fc)
                row += 1

            row = 1
            col = 2
            for his in (session['prognozfakt_graph_his']):
                worksheet.write(row, col, his)
                row += 1

            # Write a total using a formula.
            worksheet.write(row, 0, 'Прогноз/Факт', bold)
            worksheet.write(row, 2, '=SUM(C2:C5)')

        
        return send_from_directory(directory=('app/reports/'), 
                                    filename=report_name, 
                                    as_attachment=True)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text