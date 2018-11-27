from graphyte import Sender


class SendMetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.g_sender = Sender('grafana_graphite', prefix='app', protocol='tcp')

    def __call__(self, request):
        self.g_sender.send(f'request.{request.method}', 1)
        response = self.get_response(request)
        self.g_sender.send(f'response.status_code.{response.status_code}', 1)

        return response
