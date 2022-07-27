from mimetypes import init
import mysql.connector

class Mysql_first:
    def __init__(self,datas):
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
        cursor.execute(sql,values)

        try:
            connection.commit()
            print("kayıt")
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
    
###

    def student_delete(self):
        student_id = self.datas["student_id"]
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = f"delete from student_table where student_id={student_id}"
        values = (student_id)
        cursor.execute(sql)

        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:    
            connection.close()
            print("bağlantıkoparıldı...")

###   

    def student_update(self):
        student_name = self.datas["student_name"]
        student_id = self.datas["student_id"]
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "update student_table Set student_name =%s where student_id=%s"
        values = (student_name,student_id)
        cursor.execute(sql,values)

        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")

###

    def teacher_register(self):
        print("veri tabanı işlemlerine geldik")
        teacher_name = self.datas["teacher_name"]
        teacher_surname = self.datas["teacher_surname"]
        teacher_title = self.datas["teacher_title"]
        teacher_phone = self.datas["teacher_phone"]
        teacher_branch = self.datas["teacher_branch"]
        print("veritabnı için değişkenlere atandı")
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "INSERT INTO teacher_table(teacher_name,teacher_surname,teacher_title,teacher_phone,teacher_branch) VALUES (%s,%s,%s,%s,%s)"
        values = (teacher_name,teacher_surname,teacher_title,teacher_phone,teacher_branch)
        cursor.execute(sql,values)
            
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")
    
###   

    def teacher_update(self):
        teacher_name = self.datas["teacher_name"]
        teacher_id = self.datas["teacher_id"]
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = "update teacher_table Set teacher_name =%s where teacher_id=%s"
        values = (teacher_name,teacher_id)
        cursor.execute(sql,values)

        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")

###

    def teacher_delete(self):
        teacher_id = self.datas["teacher_id"]
        connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
        cursor = connection.cursor()
        sql = f"delete from teacher_table where teacher_id={teacher_id}"
        print("atandı")
        # values = (teacher_id)
        print(f"atandı3{teacher_id}")
        cursor.execute(sql)
        print("atandı2")

        try:
            connection.commit()
        except mysql.connector.Error as err:
            print('hata:',err)
        finally:
            connection.close()
            print("bağlantıkoparıldı...")

