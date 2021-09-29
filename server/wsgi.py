import sys
sys.path.insert(0, '/var/www/webroot/ROOT')

activate_this = '/var/www/webroot/ROOT/flask-app/bin/python'

with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application

if __name__ == "__main__":
    application.run()