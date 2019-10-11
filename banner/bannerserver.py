#!/usr/local/bin/python3

from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from pyfiglet import Figlet

app = Flask(__name__)
CORS(app)

# some defaults
password = "stumpylongnose"




@app.route('/banner/<string:text>', methods=['GET'])
def get_task(text):
    authenticated = False
    font_style = "thin"
    format_style = "PLAIN"

    if 'password' in request.headers:
        authenticated = password == request.headers['password']
        print('welcome stumpy')
    else:
        print('invalid authentication detected')


    if authenticated:
        if 'format' in request.args:
            format_style = request.args.get('format')
        if 'font' in request.args:
            font_style = request.args.get('font')

        custom_fig = Figlet( font=font_style )
        banner = custom_fig.renderText(text)

        print(format_style, font_style)
        print(banner)

        if format_style == 'JSON':
            return jsonify({'banner': banner})
        elif format_style == 'HTML':
            return '''<html><body><pre>{0}</pre></body></html>'''.format(banner)
        else:
            return banner
    else:
        return make_response(jsonify({'error': 'Unauthorised. Authentication required'}), 401)





@app.errorhandler(404)
def not_found(error):
    print('Errorhandler not found: {0}'.format(id) )
    return make_response(jsonify({'error': '/banner: Error creating Banner' }), 404)




if __name__ == '__main__':
    app.run(debug=True)