import os
from dotenv import load_dotenv

with open('./aws/credentials.txt','r') as aws_file:
    asw_ = aws_file.read()
    
with open('./.env','w') as env_file:
    env_file.write(asw_)
    
load_dotenv()

SECRET_KEY = os.environ.get("user")
DATABASE_PASSWORD = os.environ.get("password")


print('user:',SECRET_KEY)
print('password:',DATABASE_PASSWORD)
