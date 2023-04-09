#from downloadbutton6 import mongofeed
from pymongo import MongoClient
from splittest3 import fun1, fun2
import json
from datetime import datetime
#call fun1 from file2.py
data = fun1()
hash_tag = fun2()

client = MongoClient("mongodb://localhost:27017")
print("Connection Successful")

client = MongoClient("mongodb://localhost:27017");
print("Connection Successful")
mydb = client["TWEET"]
import json

# records = json.loads(tweets_df1.to_json(orient='records'))
data = json.loads(data.to_json(orient='records'))
from datetime import datetime

Date = datetime.now().strftime('%d-%m-%Y')
dict1 = {"Scraped Word": hash_tag, "Scraped Date": Date, "Data": data}
mydb.mycol.insert_many([dict1])
