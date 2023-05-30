import os
import json
import pandas as pd
from pymongo import MongoClient

with open("2018.json", "r", encoding="utf-8") as f:
    data = json.load(f)
df1 = pd.DataFrame(data)
df1 = df1.iloc[2:]
df1.columns = ["노선", "상대공항", "운항(편)", "여객(명)", "화물(톤)"]
df1 = df1.reset_index(drop=True)
df1["상대공항코드"] = df1["상대공항"].apply(lambda x: x.split("(")[1].replace(")", ""))

df2 = pd.read_csv("dataset.csv")

merged_df = pd.merge(df1, df2, left_on="상대공항코드", right_on="공항코드1(IATA)", how="inner")

merged_df["여객(명)"] = pd.to_numeric(merged_df["여객(명)"], errors="coerce")

top10_df = merged_df.nlargest(10, "여객(명)")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg


HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
print("Connected to MongoDB....")

db = client["project"]
db.drop_collection("match_airport")
collection = db["match_airport"]

for _, row in top10_df.iterrows():
    document = {"상대공항": row["상대공항"], "도시명": row["도시명"], "한글국가명": row["한글국가명"]}
    collection.insert_one(document)


documents = collection.find()
for document in documents:
    print(document)