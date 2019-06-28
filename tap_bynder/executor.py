import singer
import time
import hashlib
import json
from requests_oauthlib import OAuth1

from tap_kit import TapExecutor
from tap_kit.utils import transform_write_and_count, \
    format_last_updated_for_request

LOGGER = singer.get_logger()

class BydnerExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams: arr[Stream]
            args: dict
            client: BaseClient
        """
        super().__init__(streams, args, client)
        self.url = (f'https://{self.config.get("accountdomain")}.getbynder.com/'
                    f'api/v4/media/')

    def build_headers(self):
        """Authorization occurs via OAuth1 headers"""
        oauth_consumer_key = self.config.get('consumer_key')
        consumer_secret = self.config.get('consumer_secret')
        oauth_token = self.config.get('token_key')
        token_secret = self.config.get('token_secret')
        return OAuth1(oauth_consumer_key, consumer_secret, oauth_token,
                      token_secret)

    def call_incremental_stream(self, stream):
        """Method to call all incremental streams"""
        last_updated = format_last_updated_for_request(
            stream.update_and_return_bookmark(), self.replication_key_format)
        logger.info(f'the last updated time is {last_updated}')
        request_config = {
            "url": self.url,
            "headers": self.build_headers(),
            "params": self.build_params(stream, last_updated=last_updated),
            "run": True
        }

        while request_config['run']:
            res = self.client.make_request(request_config)

            if res.status_code != 200:
                raise AttributeError(f'Received status_code {res.status_code}')

            records = res.json()
            transform_write_and_count(stream, records)

            last_updated = self.get_latest_for_next_call(
                records,
                stream.stream_metadata['replication-key'],
                last_updated
            )
            stream.update_bookmark(last_updated)

            request_config = self.update_for_next_call(
                res,
                request_config
            )

        return last_updated

    def call_full_stream(self, stream):
        """Method to call all fully synched streams"""
        request_config = {
            "url": self.url,
            "headers": self.build_headers(),
            "params": self.build_params(stream),
            "run": True
        }

        while request_config['run']:
            res = self.client.make_request(request_config)

            if res.status_code != 200:
                raise AttributeError(f'Received status_code {res.status_code}')

            records = res.json()
            transform_write_and_count(stream, records)
            request_config = self.update_for_next_call(
                res,
                request_config
            )

    def build_params(self, stream, last_updated=None):
        """Set initial parameters"""
        return {
            "limit": 1000,
            "dateCreated": last_updated,
            "page": 1
        }

    def update_for_next_call(self, res, request_config):
        request_config['params']['page'] += 1
        if len(res.json()) < request_config['params']['limit']:
            request_config['run'] = False
        return request_config
