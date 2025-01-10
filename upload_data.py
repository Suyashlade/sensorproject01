from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://suyashpw:9307371441@cluster0.x4xpc.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(uri)

DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df=pd.read_csv("C:\Users\Suyash\Documents\sensorfaultdetectionpwskills\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)