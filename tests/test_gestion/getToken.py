import requests


url = "https://getoken-dev.apps.kubedev.hologram.cd/Token"
headers = {'Content-Type': 'application/json; charset=utf-8'}


def generate_token():
    body = {
        "app_id": "api-utilisateur",
        "password": "qwxszauhygtrecvbn9856"
    }

    response = requests.post(url, headers=headers, json=body).json()
    token = (response['content']['accessToken'])
    return token


TOKEN = generate_token()
print(TOKEN)
