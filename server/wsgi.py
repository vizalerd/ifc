import os,sys
virtenv = os.path.expanduser('~') + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    if sys.version.split(' ')[0].split('.')[0] == '3':
        exec(compile(open(virtualenv, "rb").read(), virtualenv, 'exec'), dict(__file__=virtualenv))
    else:
        execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

sys.path.append(os.path.expanduser('~'))
sys.path.append(os.path.expanduser('~') + '/ROOT/')

os.environ['FLASK_SETTINGS_MODULE'] = 'ROOT.settings'

from app import app as application

if __name__ == "__main__":
    application.run()