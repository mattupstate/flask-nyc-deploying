# -*- coding: utf-8 -*-
"""
    Example Flask app
    ~~~~~~~~~~~~~~~~~
"""
from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)
app.config.from_envvar('FLASK_SETTINGS_FILE', silent=True)

@app.route('/')
@app.route('/<path:path>')
def catch_all(path=''):
    return 'Hello Jupiter > %s' % app.config['CONFIG_OPTION']

if __name__ == '__main__':
    app.run()
