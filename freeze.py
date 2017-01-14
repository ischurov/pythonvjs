from flask_frozen import Freezer

from pythonvjs import app

freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'docs/pythonvjs'

if __name__ == '__main__':
    freezer.freeze()

