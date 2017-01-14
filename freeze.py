from flask_frozen import Freezer
import os

from pythonvjs import app
from shutil import move, rmtree
freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'docs'

if __name__ == '__main__':
    if os.path.isdir(os.path.join("docs", "pythonvjs", "show")):
        rmtree("docs/")
    freezer.freeze()
    move(os.path.join("docs","pythonvjs", "show"), "docs")
    rmtree(os.path.join("docs", "pythonvjs"))
