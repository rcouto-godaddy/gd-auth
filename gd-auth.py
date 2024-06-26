import requests
import json
import pprint as pp

def get_svc_acct_password(filename="", acct=""):
    with open(filename) as f:
        s = f.read()
        s_json = json.loads(s)
        return s_json[acct]

url_auth_token = "https://sso.godaddy.com/v1/api/token"
url_net_commander = "https://ncm.int.godaddy.com/api/v1.0/netcommander/run/"
url_domainbox = "https://live.domainbox.net"

payload = json.dumps({
  "username": "SVCN4if2MQL4Nemzm",
  "password": "fK2B@sCuns901-?-",
  "realm": "jomax"
})
headers = {
  'Content-Type': 'application/json'
}
 
response = requests.post(url_auth_token, headers=headers, data=payload)
# sso_token = response.json()['data']
sso_token = response.json()

## Example response from SSO API:
# print(sso_token['data'])

pswd = get_svc_acct_password("svc-accts.local", "account")
pp.pprint(pswd)