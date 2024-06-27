import requests
import json

def get_svc_acct_password(filename, acct):
  with open(filename) as f:
      s = f.read()
      s_json = json.loads(s)
      return s_json[acct]

def get_sso_token(url, headers, payload):
  response = requests.post(url, headers=headers, data=payload)
  sso_token = response.json()['data']
  return sso_token
