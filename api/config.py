import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
db_name = os.getenv('DB_NAME')

user_test = os.getenv('USER_TEST')
password_test = os.getenv('PASSWORD_TEST')
host_test = os.getenv('HOST_TEST')
db_name_test = os.getenv('DB_NAME_TEST')
