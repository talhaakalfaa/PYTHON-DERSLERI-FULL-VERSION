import mysql.connector
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
    
    # sql = "Select * From Products"
    # sql = "Select * From Categories"
    # sql = "Select * From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid"
    # sql = "Select Products.name,Products.price,Categories.name From Products inner join Categories on Categories.id=Products.Categoryid where Categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on C.id=p.Categoryid where p.name='samsung s8'"
    
    
    cursor.execute(sql)

    try:
        result = cursor.fetchall() 
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print('hata:', err) 
    finally:
        connection.close()
        print('database bağlantısı kapandı.')
getProducts()