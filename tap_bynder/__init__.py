from tap_kit import TapExecutor, BaseClient, main_method


STREAMS = [
    # TODO: Fill in with Bynder Streams
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
        BynderTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
