import os
import datetime

import jwt
from dotenv import load_dotenv

load_dotenv()

class Token:
    
    @staticmethod
    def generate_token(payload):
        issuedAt =  datetime.datetime.now(tz=datetime.timezone.utc)
        
        token = jwt.encode(
            payload={
                **payload,
                'exp': issuedAt + datetime.timedelta(days=7),
                'iat': issuedAt,
                'nbf': issuedAt,
            },
            key=os.getenv('JWT_SECRET_KEY')
        )
        
        return token
    
    @staticmethod
    def validate_token(token):
        try:
            data = jwt.decode(jwt=token, key=os.getenv('JWT_SECRET_KEY'), algorithms=["HS256"])
            
            return data
        except:
            return None