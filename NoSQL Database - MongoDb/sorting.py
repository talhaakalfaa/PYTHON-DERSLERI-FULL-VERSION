import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find().sort('name', -1) #sort sıralamak için vardır
# result = mycollection.find().sort('price', -1)
result = mycollection.find().sort([('name',1),('price',-1)])


for i in result:
    print(i)