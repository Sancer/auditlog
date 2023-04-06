from threading import local

_user = local()


class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # warning, this has not been tested with asynchronous configurations, it is only a proof of concept.
        _user.value = request.user
        response = self.get_response(request)
        _user.value = None
        return response


def get_current_user():
    try:
        return _user.value
    except AttributeError:
        return None
