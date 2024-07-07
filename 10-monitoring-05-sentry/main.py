import sentry_sdk

sentry_sdk.init(
    dsn="https://da7c9642718e1890e131e7843132f0c4@o4507549478420480.ingest.de.sentry.io/4507549497884752",
    environment="development",
    release="1.0",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

if __name__ == "__main__":
    division_zero = 1/3
