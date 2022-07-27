from flask import Flask,render_template, request
import sql_connect
#sql bağlantısını yapacak olan py uzntılı dosya 
import update_sql
import delete_sql
import sql2_connect
import update_sql
import update_teacher2



app = Flask(__name__)
@app.route("/") 
def index():
    return render_template("vote.html")
    #bağlantı yapılacak html dosyası yazılacak


# student api


@app.route("/studentreply",methods = ["GET","POST"])
#cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
def doctorreply():
    if request.method == "POST":
        #method kontrol edilir
        student_name = request.form.get("student_name")
        student_sur = request.form.get("student_surname")
        student_pho = request.form.get("student_phone")
        student_class = request.form.get("student_class")
        student_mail = request.form.get("student_mail")
        student_birt = request.form.get("student_birtday")
        student_epi = request.form.get("student_episode")
        #değişkenler atanır
        datas= {"student_name":student_name,"student_sur":student_sur,"student_pho":student_pho,"student_class":student_class,"student_mail":student_mail,"student_birt":student_birt,"student_epi":student_epi}
        sql_connect.Mysql_first3(datas).student_register()
        #sql bağlantı yapacak olan fonk. kullanılır
        print("bağlandı1")
        return render_template("student_reply.html",total =student_name )
        #datanın cevap vereceği html dosyası yazılır 
    else:
        return render_template("student_reply.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #debug doğrulama mekanizmasıdır


@app.route("/dalete",methods = ["GET","POST"])
#cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
def doctorreply():
    if request.method == "POST":
        #method kontrol edilir,
        student_id = request.form.get("student_id")
        #değişkenler atanır
        # sql_connect.Mysql_first3(datas).student_register()
        #sql bağlantı yapacak olan fonk. kullanılır
        print("başarılı1")
        return render_template("delete_reply.html",total=student_id)
        #datanın cevap vereceği html dosyası yazılır 
    else:
        return render_template("delete_reply.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #debug kontrol mekanizmasıdır




@app.route("/updatereply",methods = ["GET","POST"])
#cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
def doctorreply():
    if request.method == "POST":
        #method kontrol edilir,
        student_name = request.form.get("student_name")
        student_id = request.form.get("student_id")
        #değişkenler atanır
        update_sql.Sql_update(student_name,student_id).updata_attempt2()
        #sql bağlantı yapacak olan fonk. kullanılır
        print("başarılı1")
        return render_template("update_reply.html",total=student_name)
        #datanın cevap vereceği html dosyası yazılır 
    else:
        return render_template("update_reply.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #debug kontrol mekanizmasıdır




# teacher api

@app.route("/update2reply",methods = ["GET","POST"])
#cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
def doctorreply():
    if request.method == "POST":
        #method kontrol edilir,
        teacher_name = request.form.get("teacher_name")
        teacher_id = request.form.get("teacher_id")
        #değişkenler atanır
        update_teacher2.Sql_updates(teacher_name,teacher_id).updata_attempt3()
        #sql bağlantı yapacak olan fonk. kullanılır
        print("başarılı1")
        return render_template("update2_reply.html",total=teacher_name)
        #datanın cevap vereceği html dosyası yazılır 
    else:
        return render_template("update2_reply.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #debug kontrol mekanizmasıdır


@app.route("/teacherreply",methods = ["GET","POST"])
#cevap verilecek html dosyasının title yazılı,hangi yol ile get/post yazılır
def doctorreply():
    if request.method == "POST":
        #method kontrol edilir
        teacher_name = request.form.get("teacher_name")
        teacher_sur = request.form.get("teacher_surname")
        teacher_title = request.form.get("teacher_title")
        teacher_phone = request.form.get("teacher_phone")
        teacher_branch = request.form.get("teacher_branch")
        datas = {"teacher_name":teacher_name,"teacher_sur":teacher_sur,"teacher_title":teacher_title,"teacher_phone":teacher_phone,"teacher_branch":teacher_branch}
        #değişkenler atanır
        sql2_connect.Mysql_first4(datas).teacher_register()
        #sql bağlantı yapacak olan fonk. kullanılır
        print("bağlandı1")
        return render_template("teacher_reply.html",total =teacher_name )
        #datanın cevap vereceği html dosyası yazılır 
    else:
        return render_template("teacher_reply.html")
if __name__ == "__main__" :
    app.run(debug=True)
    #debug kontrol mekanizmasıdır