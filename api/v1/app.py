#!/usr/bin/python3
"""Flask web application
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def teardown(error):
    """Clean-up method
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error
    """
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True)