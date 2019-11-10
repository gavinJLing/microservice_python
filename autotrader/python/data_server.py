#!/usr/local/bin/python3

from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)




@app.route('/cars/<string:text>', methods=['GET'])
def get_cars(text):

    with open('car_science_autodtrader_20191028.json', 'r') as f:
        search_result_json = f.read()

    search_result_json_obj = json.loads(search_result_json)

    return jsonify(search_result_json_obj['ads'] ), 200, {'Content-Type': 'application/json; charset=utf-8'}





@app.errorhandler(404)
def not_found(error):
    print('Errorhandler not found: {0}'.format(id) )
    return make_response(jsonify({'error': '/cars: Error obtaining data' }), 404)




if __name__ == '__main__':
    app.run(debug=True)