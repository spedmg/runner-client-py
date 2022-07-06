import os

__PRODUCTION = 'production'
__STAGING    = 'staging'
__INTEGRATION = 'integration'
__DEVELOPMENT = 'development'

RUNNER_BASE_URLS = {
    __DEVELOPMENT: 'http://localhost:3000',
    __INTEGRATION: 'https://integration.sonypicturesrunner.com',
    __STAGING:     'https://staging.sonypicturesrunner.com',
    __PRODUCTION:  'https://sonypicturesrunner.com',
}

env = os.environ.get('ENV', __PRODUCTION)
base_url = os.environ.get('RUNNER_BASE_URL', RUNNER_BASE_URLS.get(env))

username      = os.environ.get('RUNNER_USERNAME')
password      = os.environ.get('RUNNER_PASSWORD')

# authorization grant not yet supported.
client_id     = os.environ.get('RUNNER_CLIENT_ID')
client_secret = os.environ.get('RUNNER_CLIENT_SECRET')
