from mimetypes import init
import mysql.connector

class Mysql_first3:
    def __init__(self,datas):
    # def __init__(self,veri1,veri2,veri3,veri4,veri5,veri6,veri7):
        self.datas=datas
        
    def student_register(self):
        student_name = self.datas["student_name"]
        student_surname = self.datas["student_surname"]
        student_phone = self.datas["student_phone"]
        student_class = self.datas["student_class"]
        student_mail = self.datas["student_mail"]
        student_birtday = self.datas["student_birtday"]
        student_episode = self.datas["student_episode"]
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "INSERT INTO student_table(student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode)
        # values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5,self.veri6,self.veri7)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("kayıt")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
    
    def student_delete(students_id):
        #init ()
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "delete from student_table where student_id=%s "
        #sql = "INSERT INTO student_table(student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5,self.veri6,self.veri7)
        values = (students_id,)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("başarılı2")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
    
    def student_update(self):
        #init ()
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "update student_table Set student_name =%s where student_id=%s"
        #sql = "INSERT INTO student_table(student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5,self.veri6,self.veri7)
        values = (self.veri1,self.veri2)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("başarılı2")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")

    def teacher_register(self):
        teacher_name = self.datas["student_name"]
        teacher_surname = self.datas["student_surname"]
        teacher_title = self.datas["teacher_title"]
        teacher_phone = self.datas["teacher_phone"]
        teacher_branch = self.datas["teacher_branch"]

        print("yazma başladı")
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        print("veritabanına bağlandı")
        sql = "INSERT INTO teacher_table(teacher_name,teacher_surname,teacher_title,teacher_phone,teacher_branch) VALUES (%s,%s,%s,%s,%s)"
        values = (teacher_name,teacher_surname,teacher_title,teacher_phone,teacher_branch)
        print("veriler hazırlandı")
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("kayıt")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
    
    def teacher_update(self):
        #init ()
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "update teacher_table Set teacher_name =%s where teacher_id=%s"
        #sql = "INSERT INTO student_table(student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5,self.veri6,self.veri7)
        values = (self.veri1,self.veri2)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("başarılı2")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
