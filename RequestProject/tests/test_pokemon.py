import requests
import pytest
HOST='https://api.pokemonbattle.me:9104'

def test_StatusCode():
    response=requests.get(url=f'{HOST}/trainers', params={'trainer_id': 2602}, timeout=5)
    assert response.status_code==200, 'Unexpected status code for /trainers'
    assert response.json()['trainer_name']=='Я вернулся', ''