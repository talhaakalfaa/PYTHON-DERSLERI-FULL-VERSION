import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
    cursor = connection.cursor()


    # cursor.execute('Select * From Products') # * burda 5 bütün kolonları al demek oluyor.
    cursor.execute('Select name,price From Products') # burda sadece almak istedğimiz kolonları alırız.

    result = cursor.fetchall() # fetchall(): çalıştırdığın SQL sorgusundan dönen tüm satırları bir liste halinde Python'a çeken komuttur.
    # result = cursor.fetchone() #fetchone(): Sorgu sonucunda 100 tane kayıt bile olsa, fetchone() dediğinde sadece ilk satırı getirir.
  
   

   
    for product in result:
        print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
        # print(f'name: {product[0]} price: {product[1]}')

getProducts()


def getProductById(id):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "12345", database = "node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s " #***where filtrelemek için kullanılır***.
    params = (id,)

    cursor.execute(sql,params)

    # cursor.execute("Select * From Products Where id=1") # * burda 5 bütün kolonları al demek oluyor.
    # cursor.execute('Select name,price From Products') # burda sadece almak istedğimiz kolonları alırız.

    result = cursor.fetchall() # fetchall(): çalıştırdığın SQL sorgusundan dönen tüm satırları bir liste halinde Python'a çeken komuttur.
    
  
    # result = cursor.fetchone() #fetchone(): Sorgu sonucunda 100 tane kayıt bile olsa, fetchone() dediğinde sadece ilk satırı getirir.
    # print(f'name: {result[0]} price: {result[1]}')

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')
   
getProductById(3)