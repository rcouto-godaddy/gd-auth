import requests
import json
 
url = "https://sso.godaddy.com/v1/api/token"
 
payload = json.dumps({
  "username": "example_username",
  "password": "example_password",
  "realm": "jomax"
})
headers = {
  'Content-Type': 'application/json'
}
 
response = requests.request("POST", url, headers=headers, data=payload)
sso_token = response.json()['data']
 
 
## Example response from SSO API:
print(response.json())
{
  'type': 'signed jwt',
  'id': 'abcde_example',
  'code': 1,
  'message': 'Success',
  'data': 'token_value_is_returned_as_data'
}
