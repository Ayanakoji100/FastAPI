from dotenv import load_dotenv
import os
load_dotenv()
dburl = os.getenv("DB_URL")
secret_key = os.getenv("SECRET_KEY")
algo = os.getenv("ALGO")
time_to_expire = int(os.getenv("TIME_TO_EXPIRE"))