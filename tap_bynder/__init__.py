from tap_kit import TapExecutor, BaseClient, main_method
from .executor import BydnerExecutor
from .assets import AssetsStream


STREAMS = [
    AssetsStream
]


REQUIRED_CONFIG_KEYS = [
    'consumer_secret',
    'consumer_key',
    'accountdomain',
    'token_key',
    'token_secret',
]


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        BydnerExecutor,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
