from urllib.parse import urlparse, parse_qs

def parseUrlData(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    params = parse_qs(parsed_url.query)
    for i in params.keys():
        params[i] = params[i][0]
    return path, params
