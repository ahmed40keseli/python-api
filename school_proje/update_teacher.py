# from flask import Flask,render_template, request
# import update_teacher2

# #sql bağlantısını yapacak olan py uzntılı dosya 

# app = Flask(__name__)
# @app.route("/") 
# def index():
#     return render_template("vote.html")
#     #bağlantı yapılacak html dosyası yazılacak

# @app.route("/update2ereply",methods = ["GET","POST"])
# #cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
# def doctorreply():
#     if request.method == "POST":
#         #method kontrol edilir,
#         teacher_name = request.form.get("teacher_name")
#         teacher_id = request.form.get("teacher_id")
#         #değişkenler atanır
#         update_teacher2.Sql_updates(teacher_name,teacher_id).updata_attempt3()
#         #sql bağlantı yapacak olan fonk. kullanılır
#         print("başarılı1")
#         return render_template("update2_reply.html",total=teacher_name)
#         #datanın cevap vereceği html dosyası yazılır 
#     else:
#         return render_template("update2_reply.html")
# if __name__ == "__main__" :
#     app.run(debug=True)
#     #debug kontrol mekanizmasıdır