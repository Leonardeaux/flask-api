import werkzeug
import os
import json
from werkzeug.local import LocalProxy
from werkzeug.utils import secure_filename
from typing import Dict, Any, List

TMP_FOLDER = '/Users/enzoleonardo/PycharmProjects/flask-api/tmp/'
UPLOAD_FOLDER = '/Users/enzoleonardo/PycharmProjects/flask-api/final/'
ALLOWED_EXTENSIONS = {'txt', 'csv'}


def allowed_file(filename: str) -> bool:
    """Verify if a file is in allowed dictionary"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def file_verification(a_request: werkzeug.local.LocalProxy) -> Dict[str, Any]:
    """Verify if a file is in the body, is not empty"""
    if a_request.method == 'POST':
        if 'file' not in a_request.files:
            return {
                'is_valid': False,
                'message': 'No file part',
                'status_code': 403
            }
        file = a_request.files['file']

        if file.filename == '':
            return {
                'is_valid': False,
                'message': 'No selected file',
                'status_code': 403
            }

        if not allowed_file(file.filename):
            return {
                'is_valid': False,
                'message': 'No allowed file',
                'status_code': 403
            }

        filename = secure_filename(file.filename)
        fullpath = os.path.join(TMP_FOLDER, filename)
        file.save(fullpath)
        return {
            'is_valid': True,
            'message': 'File uploaded',
            'status_code': 200,
            'filepath': fullpath
        }

    return {
        'is_valid': False,
        'message': 'Forbidden method',
        'status_code': 403
    }


def json_to_arguments(json_str: str) -> List[str]:
    """Convert a json struct to a list"""
    json_object = json.loads(json_str)
    if len(json_object) > 1:
        return []
    return list(json_object.items())[0][1]
