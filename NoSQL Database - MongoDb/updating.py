import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# mycollection.update_one(  #update_one:update_one():MongoDB'de belirlediğin filtreye uyan ilk ve tek bir dokümanı değiştirmek veya güncellemek için kullanılır.
#     {'name': 'Samsung S6'},
#     {'$set': {
#         'name': 'Iphone 8',
#         'price': 5000
#     }}
# )

# mycollection.update_many(  #update_many():MongoDB'de belirlediğin bir filtreye uyan tüm kayıtları tek bir seferde güncellemek için kullanılır.
#     {'name': 'Samsung S7'},
#     {'$set': {  #$set:bir dokümanı güncellerken dokümanın tamamını silip değiştirmek yerine, sadece senin belirttiğin alanları (field) değiştirmene yarar.
#         'name': 'Iphone 10',
#         'price': 10000
#     }}
# )


query = {'name': 'Samsung S7'}
newvalues = {'$set': {
                'name': 'Iphone 10',
                'price': 10000
            }}

result = mycollection.update_many(query, newvalues)

print(f'{result.modified_count} adet kayıt güncellendi')  #modified_count:bir güncelleme işlemi yaptıktan sonra, veritabanında gerçekten kaç tane dokümanın değiştirildiğini sana söyleyen bir sayıdır.

for i in mycollection.find():
    print(i)

