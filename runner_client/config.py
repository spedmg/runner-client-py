import os

base_url = os.environ.get('RUNNER_BASE_URL', 'https://sonypicturesrunner.com')

username      = os.environ.get('RUNNER_USERNAME')
password      = os.environ.get('RUNNER_PASSWORD')
client_id     = os.environ.get('RUNNER_CLIENT_ID')
client_secret = os.environ.get('RUNNER_CLIENT_SECRET')
