import mysql.connector

def insertProducts(name, price ,imageUrl ,description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app") #connect: Veritabanına giden yoldur.
    cursor = connection.cursor() #cursor:veritabanı üzerinde verileri taşıyan kamyondur.

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" #INSERT INTO: bir veritabanı tablosuna yeni bir satır (kayıt) eklemek için kullanılan SQL komutudur.
    values = (name, price ,imageUrl ,description)

    cursor.execute(sql,values) #execute(): fonksiyonu, hazırladığın SQL komutunun veritabanı üzerinde fiilen çalıştırılmasını sağlar.

    try:
        connection.commit() #commit(): komutu, veritabanı üzerinde yaptığın değişiklikleri (ekleme, silme, güncelleme) kalıcı olarak kaydetmek ve onaylamak için kullanılır.
        print(f'{cursor.rowcount} tane kayıt eklendi') #rowcount: özelliği, veritabanında çalıştırdığın son SQL komutundan kaç tane satırın etkilendiğini sana sayı olarak verir.
        print(f'son eklenen kaydın id: {cursor.lastrowid}') #cursor.lastrowid:Yeni eklenen satırın "id" değerini program tarafında öğrenmeni sağlar.
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close() #close:MySQL veritabanı arasındaki açık olan iletişim kanalını tamamen kapatır.
        print('database bağlantısı kapandı.')



def insertProducts(list):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values) #executemany():birden fazla veri kümesi için tek seferde çalıştırmanı sağlar.
    
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

list = []
while True:
    name = input('Ürün adı: ')
    price = float(input('Ürün fiyatı: '))
    imageUrl = input('Ürün resim adı: ')
    description = input('Ürün açıklaması: ')

    insertProducts(name, price, imageUrl, description) # böyle kullanırsak her seferinde database gitmek zorunda kalırız uzun sürer.
    
    list.append((name, price ,imageUrl ,description)) # böyle kullanırsak her seferinde database gitmek zorunda kalmayız liste içinde tutar en son aktarırız.

    result = input('devam etmek istiyor musunuz ? (e/h)')
    if result == 'h':
        print('Kayıtlarınız veritabanına aktarılıyor')
        print(list)
        insertProducts(list)
        break



# insertProduct(name, price, imageUrl, description)
    