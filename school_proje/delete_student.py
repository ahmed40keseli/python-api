# from flask import Flask,render_template, request
# import delete_sql

# #sql bağlantısını yapacak olan py uzntılı dosya 

# app = Flask(__name__)
# @app.route("/") 
# def index():
#     return render_template("vote.html")
#     #bağlantı yapılacak html dosyası yazılacak

# @app.route("/dalete",methods = ["GET","POST"])
# #cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
# def doctorreply():
#     if request.method == "POST":
#         #method kontrol edilir,
#         student_id = request.form.get("student_id")
#         #değişkenler atanır
#         #delete_sql.Sql_delete(student_id).updata_attempt3()
#         delete_sql.delete_attempt3
#         #sql bağlantı yapacak olan fonk. kullanılır
#         print("başarılı1")
#         return render_template("delete_reply.html",total=student_id)
#         #datanın cevap vereceği html dosyası yazılır 
#     else:
#         return render_template("delete_reply.html")
# if __name__ == "__main__" :
#     app.run(debug=True)
#     #debug kontrol mekanizmasıdır