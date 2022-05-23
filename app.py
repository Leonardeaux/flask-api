
from flask import Flask, render_template, jsonify

server = Flask(__name__)


@server.route('/')
def hello_world():
    return 'Hello World!'


@server.route('/health')
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)


# @server.route('/compute', methods=['POST', 'GET'])
# def meteo():
#     dictionnaire = {
#         'type': 'Prevision de temperature',
#         'valeurs': [24, 24, 25, 26, 27, 28],
#         'unite': "degres Celcius"
#     }
#     return jsonify(dictionnaire)


@server.route('/api/meteo/')
def meteo():
    dictionnaire = {
        'type': 'Prevision de temperature',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degres Celcius"
    }
    return jsonify(dictionnaire)


if __name__ == '__main__':
    server.run()