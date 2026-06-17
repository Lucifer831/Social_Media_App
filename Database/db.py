from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

link = os.getenv("DATABASE")

client = MongoClient(link)

db = client["SOCIAL_Media"]

Collection = db["data_info"]
