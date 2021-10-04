from flask import send_from_directory


def download_file(report_name):
    import os
    from app import app
    try:
        print(report_name)
        return send_from_directory(directory=os.path.dirname(app.instance_path), 
                                    filename=report_name, 
                                    as_attachment=True)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
