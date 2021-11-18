import json
from unittest.mock import patch
from mamba import description, context, it, before, after
from expects import *
import requests
import requests_mock
from datetime import datetime

from runner_client import auth as subject
from runner_client import config

test_url = 'https://test.url'
test_username = 'runner_user'
test_password = 'runner_password'
client_id     = 'jeanLucPicard'
client_secret = 'iAmLocutusOfBorg'

with description('runner_client.auth') as self:
    with before.each:
        self.response_body = {
                'access_token': 'runnerAccessToken',
                'refresh_token': 'runnerRefreshToken',
                'created_at': int(datetime.now().timestamp()),
                'expires_in': 3600,
            }
        self.mocks = []
        self.mocks.append(patch.object(config, 'base_url', test_url))
        self.mocks.append(patch.object(config, 'username', test_username))
        self.mocks.append(patch.object(config, 'password', test_password))
        self.mocks.append(patch.object(config, 'client_id', client_id))
        self.mocks.append(patch.object(config, 'client_secret', client_secret))
        for m in self.mocks:
            m.start()

    with after.each:
        subject.reset()
        for m in self.mocks:
            m.stop()

    with description('.access_token()'):
        with it('fetches the access_token from runner'):
            with requests_mock.Mocker() as m:
                m.post(f'{test_url}/oauth/token', json=self.response_body)
                expect(subject.access_token()).to(equal('runnerAccessToken'))
                expect(m.last_request.json()).to(equal({ 'grant_type': 'password', 'username': test_username, 'password': test_password }))

        with it('does not make multiple requests'):
            with requests_mock.Mocker() as m:
                m.post(f'{test_url}/oauth/token', json=self.response_body)
                expect(subject.access_token()).to(equal('runnerAccessToken'))
                expect(subject.access_token()).to(equal('runnerAccessToken'))
                expect(m.call_count).to(equal(1))

        with context('when the token is expired'):
            with before.each:
                subject.set_auth_tokens({
                    'access_token': 'oldAccessToken',
                    'refresh_token': 'runnerRefreshToken',
                    'created_at': int(datetime.now().timestamp()) - 7200,
                    'expires_in': 3600,
                    })
                expect(subject.current_auth_data.token_expired()).to(be_true)

            with it('uses the refresh_token to get a new one'):
                with requests_mock.Mocker() as m:
                    m.post(f'{test_url}/oauth/token', json=self.response_body)
                    expect(subject.access_token()).to(equal('runnerAccessToken'))
                    expect(m.last_request.json()).to(equal({ 'grant_type': 'refresh_token', 'refresh_token': 'runnerRefreshToken' }))

    with description('.authorization_grant()'):
        with it('fetches auth for OAuth2 Authorization grant'):
            with requests_mock.Mocker() as m:
                m.post(f'{test_url}/oauth/token', json=self.response_body)
                code = 'geordiLaForge123'
                redirect_uri = 'mock://enterprise.warp'
                subject.authorization_grant(code, redirect_uri)
                expect(subject.current_auth_data.access_token).to(equal('runnerAccessToken'))
                expect(m.last_request.json()).to(equal({
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'redirect_uri': redirect_uri,
                    'code': code,
                    'grant_type': 'authorization_code'
                    }))

    with description('.AuthData'):
        with before.each:
            self.access_token = 'myAccessToken'
            self.refresh_token = 'myRefreshToken'
            self.created_at = 1200
            self.expires_in = 50
            self.auth_data = {
                    'access_token': self.access_token,
                    'refresh_token': self.refresh_token,
                    'created_at': self.created_at,
                    'expires_in': self.expires_in,
                    }
            subject.set_auth_tokens(self.auth_data)

        with it('is JSON serializable'):
            expect(json.dumps(subject.current_auth_data)).to(equal(json.dumps(self.auth_data)))

        with it('has accessors for standard oauth properties'):
            auth_data = subject.current_auth_data
            expect(auth_data.access_token).to(equal(self.access_token))
            expect(auth_data.refresh_token).to(equal(self.refresh_token))
            expect(auth_data.created_at).to(equal(self.created_at))
            expect(auth_data.expires_in).to(equal(self.expires_in))
            expect(auth_data.token_expiry).to(equal(1250))
