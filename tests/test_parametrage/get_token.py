import requests

url = "https://getoken-dev.apps.kubedev.hologram.cd/Token"
headers = {'Content-Type': 'application/json; charset=utf-8'}


# # @pytest.fixture
def generate_token():
    body = {
        "app_id": "api-parametrageimpot",
        "password": "wnaqopuebrt920176en65"
    }

    response = requests.post(url, headers=headers, json=body).json()
    # print(response.status_code)
    token = (response['content']['accessToken'])
    return token


TOKEN = generate_token()
print(TOKEN)
