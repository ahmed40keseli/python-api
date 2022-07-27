# from flask import Flask,render_template, request
# import update_sql

# #sql bağlantısını yapacak olan py uzntılı dosya 

# app = Flask(__name__)
# @app.route("/") 
# def index():
#     return render_template("vote.html")
#     #bağlantı yapılacak html dosyası yazılacak

# @app.route("/updatereply",methods = ["GET","POST"])
# #cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
# def doctorreply():
#     if request.method == "POST":
#         #method kontrol edilir,
#         student_name = request.form.get("student_name")
#         student_id = request.form.get("student_id")
#         #değişkenler atanır
#         update_sql.Sql_update(student_name,student_id).updata_attempt2()
#         #sql bağlantı yapacak olan fonk. kullanılır
#         print("başarılı1")
#         return render_template("update_reply.html",total=student_name)
#         #datanın cevap vereceği html dosyası yazılır 
#     else:
#         return render_template("update_reply.html")
# if __name__ == "__main__" :
#     app.run(debug=True)
#     #debug kontrol mekanizmasıdır