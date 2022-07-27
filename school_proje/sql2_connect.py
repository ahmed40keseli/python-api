# from mimetypes import init
# import mysql.connector

# class Mysql_first4:
#     def __init__(self,veri1,veri2,veri3,veri4,veri5):
#         self.veri1=veri1
#         self.veri2=veri2
#         self.veri3=veri3
#         self.veri4=veri4
#         self.veri5=veri5
        
#     def insertdata(self):
#         init ()
#         print("yazma başladı")
#         connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
#         cursor = connection.cursor()
#         print("veritabanına bağlandı")
#         sql = "INSERT INTO teacher_table(teacher_name,teacher_surname,teacher_title,teacher_phone,teacher_branch) VALUES (%s,%s,%s,%s,%s)"
#         values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5)
#         print("veriler hazırlandı")
#         cursor.execute(sql,values)

#         try:
#             connection.commit()
#             print("kayıt")
#         except mysql.connector.Error as err:
#             print('hata:',err)
#         finally:
#             connection.close()
#             print("bağlantıkoparıldı...")