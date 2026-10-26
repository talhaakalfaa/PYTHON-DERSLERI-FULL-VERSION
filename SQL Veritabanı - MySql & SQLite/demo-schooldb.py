# 1- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Database bağlantısını oluşturunuz.

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database = "schooldb"
)

mycusor = connection.cursor() #cursor:sorgularını veritabanına götürür, çalıştırır ve gelen sonuçları Python'a geri getirir.