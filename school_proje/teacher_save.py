# from flask import Flask,render_template, request
# import sql2_connect
# #sql bağlantısını yapacak olan py uzntılı dosya 

# app = Flask(__name__)
# @app.route("/") 
# def index():
#     return render_template("vote.html")
#     #bağlantı yapılacak html dosyası yazılacak

# @app.route("/teacherreply",methods = ["GET","POST"])
# #cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
# def doctorreply():
#     if request.method == "POST":
#         #method kontrol edilir
#         teacher_name = request.form.get("teacher_name")
#         teacher_sur = request.form.get("teacher_surname")
#         teacher_title = request.form.get("teacher_title")
#         teacher_pho = request.form.get("teacher_phone")
#         teacher_branch = request.form.get("teacher_branch")
#         #değişkenler atanır
#         sql2_connect.Mysql_first4(teacher_name,teacher_sur,teacher_pho,teacher_branch,teacher_title,).insertdata()
#         #sql bağlantı yapacak olan fonk. kullanılır
#         print("bağlandı1")
#         return render_template("teacher_reply.html",total =teacher_name )
#         #datanın cevap vereceği html dosyası yazılır 
#     else:
#         return render_template("teacher_reply.html")
# if __name__ == "__main__" :
#     app.run(debug=True)
#     #debug kontrol mekanizmasıdır