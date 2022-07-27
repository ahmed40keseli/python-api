# #from mimetypes import init
# import mysql.connector

# # class Sql_delete:
# #     def __init__(self,veri1):#,veri2,veri3,veri4,veri5,veri6,veri7):
# #          self.veri1=veri1
# #     #     self.veri2=veri2
# #     #     self.veri3=veri3
# #     #     self.veri4=veri4
# #     #     self.veri5=veri5
# #     #     self.veri6=veri6
# #     #     self.veri7=veri7

# def delete_attempt3(students_id):
#         #init ()
#         connection = mysql.connector.connect(host = "sql11.freesqldatabase.com",user = "sql11507612",password = "qM15YaDJXs",database = "sql11507612")
#         cursor = connection.cursor()
#         sql = "delete from student_table where student_id=%s "
#         #sql = "INSERT INTO student_table(student_name,student_surname,student_phone,student_class,student_mail,student_birtday,student_episode) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#         #values = (self.veri1,self.veri2,self.veri3,self.veri4,self.veri5,self.veri6,self.veri7)
#         values = (students_id,)
#         cursor.execute(sql,values)

#         try:
#             connection.commit()
#             print("başarılı2")
#         except mysql.connector.Error as err:
#             print('hata:',err)
#         finally:
#             connection.close()
#             print("bağlantıkoparıldı...")



