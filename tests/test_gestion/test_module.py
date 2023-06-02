import requests
import getToken

endpoint = "https://api-utilisateur-dev.apps.kubedev.hologram.cd/ms_gestion_utilisateur/v1/"
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUeGVBNFRWUE04QjNFNEptM0JQM2tSalM3UjBOQUpKRmx4NUNoam5SOV9nIn0.eyJleHAiOjE2ODQyODE1MTQsImlhdCI6MTY4NDIzODMxNCwianRpIjoiYWIzMzBmOTctMWMxNS00MjNkLWEyYWQtNzUwMDNhYTM3ODdmIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hcHBzLmFieXN0ZXIuY29tL2F1dGgvcmVhbG1zL0RHSSIsInN1YiI6ImYzMjE0ZTMxLTU2OWItNGE2ZC1iMmM0LThjZDI3NjQyNzliMyIsInR5cCI6IkJlYXJlciIsImF6cCI6IkJBQ0tFTkQtREdJIiwic2Vzc2lvbl9zdGF0ZSI6IjY5OWY2ZWNjLTgxOWEtNGU0NS04Y2I0LTI1YTI1MDNhN2EyZiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiYXBpLWV4b25lcmF0aW9uIiwiYXBpLXZlbnRlIiwiYXBpLXBhcmFtZXRyYWdlaW1wb3QiLCJhcGktYWNjdXNlcmVjZXB0aW9uIiwiYXBpLWZpY2hlcHJpc2VjaGFyZ2UiLCJhcGktcmVjb3V2cmVtZW50cGFpZW1lbnQiLCJhcGktZW50aXRlIiwiYXBpLXJlY291cnNqdXJpZGljdGlvbm5lbCIsImFwaS1taXNlc291c2NlbGxlIiwiYXBpLWNvbnRyaWJ1YWJsZSIsImFwaS1kZW5vbmNpYXRpb24iLCJhcGktY2hhdGNvdXJyaWVyIiwiYXBpLWF2aXN0aWVyc2RldGVuZGV1ciIsImFwaS1yZWNsYW1hdGlvbmFkbWluaXN0cmF0aXZlIiwiYXBpLWVucXVldGUiLCJhcGktYXNzdWplc3Rpc3NlbWVudCIsImFwaS1yZWNvdXZyZW1lbnRlbmNhaXNzZW1lbnQiLCJhcGktZGVncmV2ZW1lbnQiLCJhcGktcG9ydGVmZXVpbGxlIiwiYXBpLXV0aWxpc2F0ZXVyIiwiYXBpLW1pc2VyZWNvdXZyZW1lbnQiLCJhcGktZW5yZWdpc3RyZW1lbnRjb3VycmllciIsImFwaS1kZWZhaWxsYW5jZSIsImFwaS1wYXJhbWV0cmFnZWFwcGxpY2F0aW9uIiwiYXBpLWFkbWlzc2lvbm5vbnZhbGV1ciIsImFwaS1jb250cmFpbnRlIiwiYXBpLWNvbXB0ZWJhbmNhaXJlIiwiYXBpLXJlZHJlc3NlbWVudCIsImFwaS1taXNzaW9uIiwiYXBpLXBhaWVtZW50ZWNoZWxvbm5lcyIsImFwaS1pbXBvc2l0aW9ub2ZmaWNlIiwibXNfdGVzdCJdfSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiNjk5ZjZlY2MtODE5YS00ZTQ1LThjYjQtMjVhMjUwM2E3YTJmIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmcm9udGVuZCJ9.JJ4BC8vhSooYlb-7Nq3xUINO_ir6Un-g-zatJwCacMzfT4Dq9AmuyXcHjWLcjdccpJAsz_P4ePVueZqFfDQz-Ch1xuikryl_iTfR4a3jr1YtorI155qPmQ7OYgP3IBAYVAe6DVTH65k4ygc5BYbwXU5mCVseBASlxBKpG1AxfAyzArrMjqRgG1Rd5C8j99lA1OH52YpNG4bCC3IcJ7DKE8CX0WY8YRsQPmdxUHeZHJf0CbWW4OC4IdaLzS9mau92Zi-jQ6Np8Wl3JvzFOHM3k98CFgYzMAeaSIh8iDTpPi4vprQu0DsxsalNhJJ1DJtDjOXwHQMhsny5h6dX8eLAPA"

headers = {'app_id_receive': 'ms_test', 'Authorized': f'Bearer {TOKEN}', 'Content-Type': 'application/json; '
                                                                                         'charset=utf-8'}


#
def test_saveModule():
    body = {
        "intitule": "Assujett",
        'fkUtilisateurCreat': "1"
    }
    get_response = requests.post(endpoint + "saveModule", headers=headers, json=body)
    assert get_response.status_code == 200
    print(get_response.json)
# print(TOKEN)
