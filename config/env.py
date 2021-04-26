import environ

env = environ.Env()

# option to attach an env file
# default location is `.env-dir/local`
# if file not found, simply ignored
env.read_env(env("ENV_FILE", default=".env-dir/local"))

DJANGO_DEBUG = env("DJANGO_DEBUG", cast=bool, default=True)
EXTRA_ALLOWED_HOSTS = env("EXTRA_ALLOWED_HOSTS", default="")  # foo.com,bar.com
