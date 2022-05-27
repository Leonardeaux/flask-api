import pandas as pd
from typing import List
from flask import Response
import utils
import os


def download_csv(process_name: str, data: pd.DataFrame, path: str) -> str:
    """Download a csv file in the server"""
    result_path = f'{utils.UPLOAD_FOLDER}{process_name}_result.csv'
    data.to_csv(result_path, index=True)
    os.remove(path)
    return result_path


def group_by_request(path: str, affected_columns: List[str]) -> Response():
    """Group by function processed on a csv file"""
    data = pd.read_csv(path)
    try:
        data_gb = data.groupby(affected_columns)
        result_path = f'{utils.UPLOAD_FOLDER}group_by_result.csv'
        try:
            with open(result_path, "w") as f:
                f.write("")
        except IOError:
            pass
        finally:
            for key, item in data_gb:
                data_gb.get_group(key).to_csv(result_path, mode='a')
            os.remove(path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')


def average_request(path: str, affected_columns: List[str]) -> Response():
    """Average function processed on a csv file"""
    if len(affected_columns) < 2:
        return Response('More than 1 parameters is needed', status=403, mimetype='application/json')

    data = pd.read_csv(path)
    try:
        data_average = data[affected_columns].groupby(by=[affected_columns[0]]).mean()
        print(data_average)
        try:
            result_path = download_csv("average", data_average, path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
        except:
            return Response('Error on download', status=500, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')


def variance_request(path: str, affected_columns: List[str]) -> Response():
    """Variance function processed on a csv file"""
    if len(affected_columns) < 2:
        return Response('More than 1 parameters is needed', status=403, mimetype='application/json')
    data = pd.read_csv(path)
    try:
        data_variance = data[affected_columns].groupby(by=[affected_columns[0]]).var()
        print(data_variance)
        try:
            result_path = download_csv("variance", data_variance, path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
        except:
            return Response('Error on download', status=500, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')


def ecart_type_request(path, affected_columns: List[str]) -> Response():
    """Ecart Type function processed on a csv file"""
    if len(affected_columns) < 2:
        return Response('More than 1 parameters is needed', status=403, mimetype='application/json')
    data = pd.read_csv(path)
    try:
        data_ecart_type = data[affected_columns].groupby(by=affected_columns[0]).std()
        print(data_ecart_type)
        try:
            result_path = download_csv("ecart_type", data_ecart_type, path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
        except:
            return Response('Error on download', status=500, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')


def stats_request(path) -> Response():
    """Stats function processed on a csv file"""
    data = pd.read_csv(path)
    try:
        res = data.describe()
        print(res)
        try:
            result_path = download_csv("stats", res, path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
        except:
            return Response('Error on download', status=500, mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')


def no_null_request(path: str, affected_columns: List[str]) -> Response():
    """Not null function processed on a csv file"""
    data = pd.read_csv(path)
    try:
        data_without_null = data.dropna(axis=0, how='any', thresh=None, subset=affected_columns, inplace=False)
        print(data_without_null)
        try:
            result_path = download_csv("not_null", data_without_null, path)
            return Response(f'File uploaded, path: {result_path}', status=200, mimetype='application/json')
        except:
            return Response('Error on download', status=500,
                            mimetype='application/json')
    except Exception as e:
        return Response(str(e), status=404, mimetype='application/json')
