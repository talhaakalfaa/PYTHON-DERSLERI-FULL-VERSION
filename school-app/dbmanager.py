import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self,connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata:', err)
    
    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)



    def getClasses(self):
        sql = "select * from class "
        self.cursor.execute(sql,)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('hata:', err)


    def getStudentsByClassId(self,classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('hata:', err)


    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber,StudentName,StudentSurname,StudentBirthdate,StudentGender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.StudentNumber,student.StudentName,student.StudentSurname,student.StudentBirthdate,student.StudentGender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)


    def editStudent(self, student: Student):
        sql = "update student set StudentNumber=%s,StudentName=%s,StudentSurname=%s,StudentBirthdate=%s,StudentGender=%s,classid=%s where id =%s"
        value = (student.StudentNumber,student.StudentName,student.StudentSurname,student.StudentBirthdate,student.StudentGender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
    
    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass
        
    def __del__(self):
        self.connection.close()
        print('db silindi')




db = DbManager(connection)

student = db.getStudentById(7)

student[0].StudentName = "İlknur"

# db.addStudent(student[0])
db.editStudent(student[0])



# students = db.getStudentsByClassId(1)
# print(students[0].StudentName)
# print(students[4].StudentName)

  
