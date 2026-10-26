import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# mycollection.delete_one({"name":"Iphone 10"}) #delete_one():MongoDB'de belirlediğin filtreye uyan ilk ve tek bir dokümanı veritabanından tamamen silmek için kullanılır.
# mycollection.delete_many({"name": {"$regex":"^S"}}) #delete_many():MongoDB'de belirlediğin filtreye uyan tüm dokümanları tek bir seferde silmek için kullanılır.
result = mycollection.delete_many({}) #bütün veriler silinir.
print(f'{result.deleted_count} adet kayıt silindi') #deleted_count:bir silme işlemi bittikten sonra MongoDB'nin sana gönderdiği "Toplamda şu kadar kayıt sildim" bilgisidir.

for i in mycollection.find():
    print(i)
