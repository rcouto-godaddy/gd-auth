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
  "password": get_svc_acct_password("svc-accts.local", "SVCN4if2MQL4Nemzm"),
  "realm": "jomax"
})

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-CSRFToken':  ''
}
 
response = requests.post(url_auth_token, headers=headers, data=payload)
sso_token = response.json()['data']

####################################################################################

payload2 = [
  {
    "device": "lbsa0101-01.mgt.sxb1.gdg",
    "config_mode": "false",
    "commands": [
      "show run"
    ]
  }
]

headers['X-CSRFToken'] = sso_token
payload2 = json.dumps(payload2)
resp = requests.request("POST", url_net_commander, headers=headers, data=payload2)

pp.pprint(sso_token)
pp.pprint(resp)