import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"]
mycollection = mydb["products"]


# result = mycollection.find_one({"name": "Samsung S5"}) #tek bir kayıt gelcekse bunu kullan.
# print(result)


# result = mycollection.find_one({"_id":ObjectId("6973f5ab9f54e80dcc8702b5")}) #ObjectId():ObjectId: MongoDB'nin otomatik oluşturduğu 24 karakterli benzersiz kimlik tipidir. Python'da ID ile arama yaparken, metin halindeki ID'yi ObjectId("...") içine alarak veritabanına göndermemiz gerekir.
# print(result)

# result = mycollection.find() #tek bir kayıt gelmicekse bunu kullan.

# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"] #$in:Bu sütun şuna veya şuna veya şuna eşit olanları getir" demenin en kısa yoludur.
#     }
# }) 

# result = mycollection.find({
#     "price": {
#         "$gt": 2000 $gt:belirlediğin değerden daha büyük olan kayıtları seçmeni sağlar.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gte": 2000 #$gte:"Büyük veya Eşittir Sınırı" olarak düşünebilirsin.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq": 2000 #$eq:belirlediğin değere birebir eşit olup olmadığını kontrol eder.
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$lte": 2000 $lte:Belirlediğin değerden hem daha küçük olanları hem de tam o değere eşit olanları seçer.
#     }
# })

# result = mycollection.find({
#     "name": {"$regex": "^S"} #$regex:Sadece tam eşleşmelere değil, kelimenin içindeki kalıplara bakmanı sağlar.


# for i in result:
#     print(i)


