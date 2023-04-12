from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_DATA_HOST = os.environ.get("MYSQL_ACCESS_DATA_USER")
print(ACCESS_DATA_HOST)