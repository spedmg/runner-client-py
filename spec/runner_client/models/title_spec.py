from mamba import description, context, it, before, after
from expects import *

from runner_client.models import Title

API_DATA = {
        'gpms_id': 1193687,
        'id': 429520,
        'gpms_id_and_name': '1193687|JUMANJI: WELCOME TO THE JUNGLE',
        'name': 'JUMANJI: WELCOME TO THE JUNGLE',
        'alpha': None,
        'eidr': '10.5240/868A-00B0-E31C-1E40-F077-T',
        'gmdm_id': 3420566,
        'full_name': 'JUMANJI: WELCOME TO THE JUNGLE',
        'season_number': None,
        'season_number_integer': None,
        'season_number_prefix': None,
        'season_number_suffix': None,
        'title_level': 'non-episodic',
        'title_type': 'feature',
        'walker_id': 'F3301700000'
        }

with description('runner_client.models.Title') as self:
    with before.each:
        self.subject = Title(**API_DATA)

    with it('has the expected attributes'):
        expect(self.subject.gpms_id).to(equal(1193687))
