import pymongo

myclient = pymongo.MongoClient("mongodb+srv://talhakalfa24:vJK0HJPgT53gMhCY@cluster0.1v9sj8y.mongodb.net/node-app?appName=Cluster0")

mydb = myclient["node-app"] #myclient:Veritabanı sunucusuna ulaşmanı sağlar.
mycollection = mydb["products"] #mydb:Verilerin asıl depolandığı "klasörü" hedef alır.

# product = {"name":"Samsung S5", "price": 2000}

# result = mycollection.insert_one(product) #insert_one():MongoDB'de bir koleksiyonun içine tek bir doküman (veri kaydı) eklemek için kullanılır.

# print(result)
# print(type(result))
# print(result.inserted_id) #inserted_id:Yeni eklenen dokümanın kimliğini (ID) anında öğrenmeni sağlar.

productlist = [
    {"name":"Samsung S6", "price": 3000, "description":"iyi telefon"},
    {"name":"Samsung S7", "price": 4000, "categories": ['telefon','elektronik']},
]

result = mycollection.insert_many(productlist) #insert_many(): MongoDB'de bir liste dolusu veriyi (dokümanı) tek bir komutla veritabanına eklemek için kullanılır.

print(result.inserted_ids) #insert_ids:Tek bir seferde eklediğin onlarca veya yüzlerce verinin her birine ulaşmanı sağlayacak "anahtarları" topluca sana teslim eder.
