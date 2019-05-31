"""
Main Application.
"""
from __future__ import absolute_import
from flask import jsonify, Flask, request
from config import DEBUG, LOG_FORMAT
from image_classification import InceptionV3Classifier
import logging
import os

# Load Inceptionv3 classifier in memory
CLASSIFIER = InceptionV3Classifier(weights='imagenet')

if DEBUG:
    loglevel = logging.DEBUG
else:
    loglevel = logging.INFO

def create_app():
    """ Create flask application. """
    app = Flask(__name__)
    app.config.from_object('config')

    @app.route('/api/1/status')
    def status():
        """ Status handler. """
        return jsonify({
            "status": "ok"
        })

    @app.route('/api/1/process')
    def process():
        """ Root handler. """
        return jsonify({
            "status": "processing"
        })
    return app

if __name__ == '__main__':
    """ Main entrypoint. """
    logging.basicConfig(level=loglevel,
                        format=LOG_FORMAT,
                        datefmt='%Y-%m-%d %H:%M:%S %z')

    app = create_app()
    print('Created app.')