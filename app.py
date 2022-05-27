from flask import Flask, jsonify, request, Response
import dataframe_processing as dp
import utils

# Clé de sécurité
Key = 'Canard'

app = Flask(__name__)


@app.before_request
def token_verification() -> Response():
    """token verification"""
    if request.headers.get('Authorization') != Key:
        return Response('Forbidden wrong token', status=403, mimetype='application/json')


@app.route('/')
def hello_world() -> Response():
    return 'Hello World!'


@app.route('/health')
def health() -> Response():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)


@app.route('/compute/groupby', methods=['GET', 'POST'])
def compute_grouby() -> Response():
    """compute route for group by process"""
    request_result = utils.file_verification(request)
    params = utils.json_to_arguments(request.form.get("params"))
    if request_result['is_valid']:
        return dp.group_by_request(request_result['filepath'], params)
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


@app.route('/compute/average', methods=['GET', 'POST'])
def compute_average() -> Response():
    """compute route for average process"""
    request_result = utils.file_verification(request)
    params = utils.json_to_arguments(request.form.get("params"))
    if request_result['is_valid']:
        return dp.average_request(request_result['filepath'], params)
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


@app.route('/compute/notnull', methods=['GET', 'POST'])
def compute_notnull() -> Response():
    """compute route for not null process"""
    request_result = utils.file_verification(request)
    params = utils.json_to_arguments(request.form.get("params"))
    if request_result['is_valid']:
        return dp.no_null_request(request_result['filepath'], params)
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


@app.route('/compute/variance', methods=['GET', 'POST'])
def compute_variance() -> Response():
    """compute route for variance process"""
    request_result = utils.file_verification(request)
    params = utils.json_to_arguments(request.form.get("params"))
    if request_result['is_valid']:
        return dp.variance_request(request_result['filepath'], params)
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


@app.route('/compute/ecart_type', methods=['GET', 'POST'])
def compute_ecart_type() -> Response():
    """compute route for ecart type process"""
    request_result = utils.file_verification(request)
    params = utils.json_to_arguments(request.form.get("params"))
    if request_result['is_valid']:
        return dp.ecart_type_request(request_result['filepath'], params)
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


@app.route('/compute/stats', methods=['GET', 'POST'])
def compute_stats() -> Response():
    """compute route for stats process"""
    request_result = utils.file_verification(request)
    if request_result['is_valid']:
        return dp.stats_request(request_result['filepath'])
    else:
        return Response(request_result['message'], status=request_result['status_code'], mimetype='application/json')


if __name__ == '__main__':
    app.run()
