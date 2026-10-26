import pymongo

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one() #find_one():Koleksiyonu tarar, aradığın şarta uyan tek bir kayıt bulur bulmaz aramayı durdurur ve o kaydı sana getirir.
for i in mycollection.find({},{"_id":0,"name":1}): #find():çoklu arama yapmak için kullanılır. 0 o sütun dışında herşeyi alır 1 dediğimzide o sütunu alır başka bişey almaz.
    print(i)

# print(result)