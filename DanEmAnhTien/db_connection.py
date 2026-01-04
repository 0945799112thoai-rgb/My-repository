import os
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    uri = os.getenv("MONGODB_URI")
    # Kết nối bằng mongoengine
    connect(host=uri, alias='default')
    print("🔥 Kết nối MongoDB Atlas thành công qua MongoEngine!")