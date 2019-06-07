import singer
import backoff
import requests

from tap_kit import BaseClient

LOGGER = singer.get_logger()


class BynderClient(BaseClient):

    @staticmethod
    def requests_method(method, request_config, body):
        return requests.request(
            method,
            request_config['url'],
            params=request_config['params'],
            auth=request_config['headers'],
            json=body)
