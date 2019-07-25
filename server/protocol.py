from datetime import datetime


def validate_request(request):
        return 'action' in request and 'time' in request


def make_response(request, code, data=None):
        return {
                'action': request.get('action'),
                'time': datetime.now().timestamp(),
                'code': code,
                'data': data,
        }


