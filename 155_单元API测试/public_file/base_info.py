
from public_file import config_info

def get_url(method):

    host = config_info.url()
    method = method
    url = ''.join([host,method])

    return url
