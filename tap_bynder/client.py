import singer
import backoff

from tap_kit import BaseClient

LOGGER = singer.get_logger()


class RateLimitException(Exception):
    pass


class BynderClient(BaseClient):

    @staticmethod
    def requests_method(method, request_config, body):
        return requests.request(
            method,
            request_config['url'],
            auth=request_config['headers'],
            params=request_config['params'],
            json=body)
