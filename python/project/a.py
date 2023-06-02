BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f: 
    secrets = json.load(f)

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
    return errorMsg

# Atlas API 정보
HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

# Secret.json의 API 키
api_key = secrets["youtube_apiKey2"]
youtube = build("youtube", "v3", developerKey=api_key)

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["project"]
    
if year == 2018:
    collection = db["collection2018"]
elif year == 2020:
    collection = db["collection2020"]
elif year == 2022:
    collection = db["collection2022"]
elif year == 2023:
    collection = db["collection2023"]
else:
    return "Invalid year"
    
# 컬렉션에서 데이터 가져오기
data = collection.find_one({}, {"_id": 0, "counts": 1})["counts"]
print(data)
