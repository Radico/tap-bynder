import singer
import time
import hashlib
from requests_oauthlib import OAuth1

from tap_kit import TapExecutor


class BydnerExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams: arr[Stream]
            args: dict
            client: BaseClient
        """
        super().__init__(streams, args, client)
        self.url = (f'https://{self.config.get("accountdomain")}.bydner.com/'
                    f'api/v4/media/')

    def build_headers(self):
        """Authorization occurs via OAuth1 headers"""
        oauth_consumer_key = self.config.get('consumer_key')
        consumer_secret = self.config.get('consumer_secret')
        oauth_token = self.config.get('token_key')
        token_secret = self.config.get('token_secret')
        return OAuth1(oauth_consumer_key, consumer_secret, oauth_token,
                      token_secret)
