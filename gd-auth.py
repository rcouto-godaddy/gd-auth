import requests
import json
import aux_functions as aux
import pprint as pp

#############################################################################################################################

url_auth_token = "https://sso.godaddy.com/v1/api/token"

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

payload = json.dumps({
  "username": "SVCN4if2MQL4Nemzm",
  "password": aux.get_svc_acct_password("svc-accts.local", "SVCN4if2MQL4Nemzm"),
  "realm": "jomax"
})
 
sso_token = aux.get_sso_token(url_auth_token, headers, payload)

#############################################################################################################################

url_netcommander = "https://ncm.int.godaddy.com/api/v1.0/netcommander/run/"

# Python list with commands; example: commands = [ "show version", "show clock"
commands = ["show version"]

payload_netcommander = [
  {
    "device": "lbsa0101-01.mgt.sxb1.gdg",
    "config_mode": "false",
    "commands": commands
  }
]

headers_netcommander = {
  'Content-Type': 'application/json',
  'Authorization': f'sso-jwt {sso_token}' 
}

response = requests.request("POST", url_netcommander, headers=headers_netcommander, data=json.dumps(payload_netcommander))
print(response.status_code)
result = response.json()

print(json.dumps(result, indent=8))