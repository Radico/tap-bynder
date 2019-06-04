from tap_kit import TapExecutor, BaseClient, main_method


STREAMS = [
    # TODO: Fill in with Bynder Streams
]


REQUIRED_CONFIG_KEYS = [] # TODO: Config correctly


class BynderTap(TapExecutor):
    url = ''
    pagination_type = 'next'
    auth_type = 'basic'


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        BynderTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
