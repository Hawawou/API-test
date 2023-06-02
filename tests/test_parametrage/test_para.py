import requests
import get_token

endpoint = "https://api-parametrageimpot-dev.apps.kubedev.hologram.cd/api/nature_impot"

TOKEN = get_token.generate_token()
headers = {'app_id_receive': 'ms_test', 'Authorized': f'Bearer {TOKEN}',
           'Content-Type': 'application/json; charset=utf-8'}


# Save module
# def test_post():
#     body = {
#         'fk_agent': 5,
#         'intitule': 'TVA4',
#         'description': 'Lorem ipsum'
#     }

#     response = requests.post(endpoint, headers=headers, json=body)
#     assert response.status_code == 200
#     data = response.json()
#     print(data)


def test_getAll():
    get_response = requests.get(endpoint, headers=headers)
    assert get_response.status_code == 200
    print(get_response.json)
