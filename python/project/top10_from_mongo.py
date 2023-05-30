#FastAPI사용해서 Mongo에 있는 database: project / documents: top10_cities 
import os
import json
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

HOSTNAME = secrets.get("ATLAS_Hostname")
USERNAME = secrets.get("ATLAS_Username")
PASSWORD = secrets.get("ATLAS_Password")

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["project"]
collection = db["top10_cities"]

@app.get("/top10_cities")
def get_documents():
    documents = collection.find()  # 상위 몇개 조회시 collection 에다가 넣기
    result = []
    for document in documents:
        document["_id"] = str(document["_id"])
        result.append(document)
    return result