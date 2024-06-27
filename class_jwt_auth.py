#generate_token.py
#==========================
import subprocess
from dataclasses import dataclass
@dataclass
class JWT_generator:
    jwt_env: str
def generate_token(self):
        try:
            jwt_result = subprocess.run(['./ssojwt' , '--environment', self.jwt_env] ,  capture_output=True, text=True)
        except FileNotFoundError as e:
            print(f"ERROR - please ensure to have ssojwt in the same folder to be used with this tool")
            return('EXCEPTION')
        if jwt_result.stdout == '':
            return('ERROR')
        else:
            return (jwt_result.stdout.strip())

