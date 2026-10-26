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

def getProducts():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
    cursor = connection.cursor()


    # cursor.execute('Select * From Products') # * burda 5 bütün kolonları al demek oluyor.
    cursor.execute('Select * From Products Order By name, price') # burda sadece almak istedğimiz kolonları alırız.

    #order by:Karışık gelen verileri (isim, fiyat, tarih vb.) senin istediğin mantığa göre dizmeni sağlar.
    #ASC:azalandan artana göre dizer. 
    #DESC:artandan azalana göre dizer. 
    
    try:
        result = cursor.fetchall() # fetchall(): çalıştırdığın SQL sorgusundan dönen tüm satırları bir liste halinde Python'a çeken komuttur.
        # result = cursor.fetchone() #fetchone(): Sorgu sonucunda 100 tane kayıt bile olsa, fetchone() dediğinde sadece ilk satırı getirir.
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
        # print(f'name: {product[0]} price: {product[1]}')
    except mysql.connector.Error as err:
        print('hata:', err) 
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def getProductById(id):

    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s "
    params = (id,)

    cursor.execute(sql,params)

    # cursor.execute("Select * From Products Where id=1") # * burda 5 bütün kolonları al demek oluyor.
    # cursor.execute('Select name,price From Products') # burda sadece almak istedğimiz kolonları alırız.

    result = cursor.fetchall() # fetchall(): çalıştırdığın SQL sorgusundan dönen tüm satırları bir liste halinde Python'a çeken komuttur.
    
  
    # result = cursor.fetchone() #fetchone(): Sorgu sonucunda 100 tane kayıt bile olsa, fetchone() dediğinde sadece ilk satırı getirir.
    # print(f'name: {result[0]} price: {result[1]}')

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')
   
   
def updateProduct(id, name, price):
        connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
        cursor = connection.cursor()

        
        sql = "Update products Set name=%s, price=%s Where id=%s"
        values = (name, price, id)
        cursor.execute(sql, values)

        try:
            connection.commit() #commit(): komutu, veritabanı üzerinde yaptığın değişiklikleri (ekleme, silme, güncelleme) kalıcı olarak kaydetmek ve onaylamak için kullanılır.
            print(f'{cursor.rowcount} tane kayıt güncellendi') #rowcount: özelliği, veritabanında çalıştırdığın son SQL komutundan kaç tane satırın etkilendiğini sana sayı olarak verir.
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            connection.close() #close:MySQL veritabanı arasındaki açık olan iletişim kanalını tamamen kapatır.
            print('database bağlantısı kapandı.')

updateProduct(1, '', 35000)
getProducts()

