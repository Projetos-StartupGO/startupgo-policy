class RequestException(Exception):
    pass


class APIException(RequestException):
    "Handle 4xx and 5xx errors from the SparkPost API"

    def __init__(self, response, *args, **kwargs):
        # noinspection PyBroadException
        try:
            errors = response.json()['errors']
            error_template = "{message} Code: {code} Description: {desc} \n"
            errors = [error_template.format(message=e.get('message', ''),
                                            code=e.get('code', 'none'),
                                            desc=e.get('description', 'none'))
                      for e in errors]
        # TODO: select exception to catch here
        except:  # noqa: E722
            errors = [response.text or ""]
        self.status = response.status_code
        self.response = response
        self.errors = errors
        message = """Call to {uri} returned {status_code}, errors:
        {errors}
        """.format(
            uri=response.url,
            status_code=response.status_code,
            errors='\n'.join(errors)
        )
        super().__init__(message, *args, **kwargs)


class RequestsTransport(object):
    def __init__(self):
        import requests
        self.sess = requests.Session()

    def request(self, method, uri, headers, **kwargs):
        response = self.sess.request(method, uri, headers=headers, **kwargs)
        if response.status_code == 204:
            return True
        if not response.ok:
            raise APIException(response)
        if 'results' in response.json():
            return response.json()['results']
        return response.json()

    def options(self, headers, **kwargs):
        return self.request('OPTIONS', headers, **kwargs)

    def get(self, uri, headers, **kwargs):
        return self.request('GET', uri, headers, **kwargs)

    def post(self, uri, headers, **kwargs):
        return self.request('POST', uri, headers, **kwargs)

    def put(self, uri, headers, **kwargs):
        return self.request('PUT', uri, headers, **kwargs)

    def patch(self, uri, headers, **kwargs):
        return self.request('PATCH', uri, headers, **kwargs)

    def delete(self, uri, headers, **kwargs):
        return self.request('DELETE', uri, headers, **kwargs)
