# 1- workbench IDE ile schooldb bir database oluşturup student tablosuna
    # Id,StudentNumber,Name,Surname,Birthdate,Gender 

# 2- database bağlantısını oluşturunuz.

# 3-  aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.


    
import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,Studentnumber,Studentname,Studentsurname,Studentbirthdate,Studentgender):
        self.id = id
        self.StudentNumber = Studentnumber
        self.StudentName = Studentname
        self.StudentSurname = Studentsurname
        self.StudentBirthdate = Studentbirthdate
        self.StudentGender = Studentgender
        
    
    def saveStudent(self):
        sql = "INSERT INTO Student(id,StudentNumber,StudentName,StudentSurname,StudentBirthdate,StudentGender) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (self.StudentNumber,self.Studentname,self.Studentsurname,self.Studentbirthdate,self.Studentgender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

        selin = Student(
            "101",
            "Selin",
            "Oğuz",
            datetime(2007, 2, 27),
            "K"
        )
        selin.saveStudent()
        @staticmethod
        def saveStudent(self):
            sql = "INSERT INTO Student(id,StudentNumber,StudentName,StudentSurname,StudentBirthdate,StudentGender) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (self.StudentNumber,self.Studentname,self.Studentsurname,self.Studentbirthdate,self.Studentgender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

        selin = Student(
            "101",
            "Selin",
            "Oğuz",
            datetime(2007, 2, 27),
            "K"
        )
        selin.saveStudent()        

    
        # ogrenciler = [
        #     (1,"101","Selin","Oğuz",datetime(2007, 2, 27), "K"),
        #     (2,"102","Çağan","Kalfa",datetime(1998, 8, 20), "E"),
        #     (3,"103","Bülent","İlhan",datetime(2025, 4, 21), "E"),
        #     (4,"104","Ecem","Düdükçü",datetime(2002, 6, 29), "K"),
        #     (5,"105","İbrahim","Oğuz",datetime(2002, 7, 16), "E"),
        #     (6,"106","Talha","Kalfa",datetime(2006, 5, 24), "E")
        # ]

        # mycursor.executemany(sql, ogrenciler)


# 4- Aşağıdaki sorguları yazınız
#   a- Tüm öğrenci kayıtlarını alınız.
#   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
#   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
#   d- 2002 doğumlu öğrenci bilgilerini alınız.  
#   e- İsmi Selin ve doğum tarihi 2007 olan öğrenci bilgilerini alınız.
#   f- adı içinde 'ta' ifadesi geçen kayıtları alınız.
#   g- Kaç erkek öğrenci vardır ?
#   h- Kız öğrencilerin harf sırasına göre getiriniz.

#A'NIN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select * From student"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#B'NİN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select StudentNumber,StudentName,StudentSurname From student"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#C'NİN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select StudentName, StudentSurname From student Where StudentGender = 'K' "

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#D'NİN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select * From student Where year(StudentBirthdate) = 2002"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#E'NİN CEVABI 
#     @staticmethod
#     def StudentInfo():
#         sql = "Select * From student Where StudentName ='Selin' and year(StudentBirthdate) = 2007"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#F'NİN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select * From student Where StudentName LIKE 'Ta%'" #% başta olursa Ta ile bitmesi gerekiyor % sonda olursa Ta ile başlamsı gerekiyor

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#G'NİN CEVABI 
#     @staticmethod
#     def StudentInfo():
#         sql = "Select COUNT(*) From student Where StudentGender = 'E'"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

#H'IN CEVABI
#     @staticmethod
#     def StudentInfo():
#         sql = "Select StudentName,StudentSurname From student Where StudentGender='K' Order By StudentName,StudentSurname"

#         Student.mycursor.execute(sql)

#         try:
#             results = Student.mycursor.fetchall()
#             print(results)
#         except mysql.connector.Error as err:
#             print('hata:', err)
#         finally:
#             Student.connection

# Student.StudentInfo()

# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet'e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Hata',err)
        
    @staticmethod
    def updateStudents(liste):
        sql = "update student set StudentNumber=%s,StudentName=%s,StudentSurname=%s,StudentBirthdate=%s,StudentGender=%s where id =%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('hata:',err)
    
    @staticmethod
    def getStudentsGender(StudentGender):
        sql = "select * from student where StudentGender=%s"
        value = (StudentGender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Hata',err)


# obj = Student.getStudentById(7)


# student = Student.getStudentById(7)
# student.StudentName = 'Selin'
# student.StudentSurname = 'Kalfa'

# student.updateStudent()

students = Student.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    liste.append(std)

Student.updateStudents(liste)