import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests

def get_url_parameter(url, parameter):
    """
    :param url: url as string
    :param parameter: parameter
    :return: list of parameter values
    """
    parsed = urlparse.urlparse(url)
    return parse_qs(parsed.query)[parameter]   # a list

def get_participant_sescodes(url, params):
    data = requests.get(url, params)
    return data.json()