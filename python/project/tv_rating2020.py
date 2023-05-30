import pandas as pd
import json
import pymongo

with open('tv_ratings2020.json') as f:
    js = json.loads(f.read())
df = pd.DataFrame(js)
print(df)


