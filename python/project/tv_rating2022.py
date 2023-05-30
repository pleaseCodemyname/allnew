import pandas as pd
import json

with open('tv_ratings2022.json') as f:
    js = json.loads(f.read())
df = pd.DataFrame(js)
print(df)


