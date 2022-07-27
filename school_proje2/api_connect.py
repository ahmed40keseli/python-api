from flask import Flask,render_template, request
import sql_connect



app = Flask(__name__)
@app.route("/") 
def index():
    return render_template("vote.html")
    


###     STUDENT APİ


@app.route("/student_register",methods = ["GET","POST"])
def student_register():
    if request.method == "POST":
        student_name = request.form.get("student_name")
        student_surname = request.form.get("student_surname")
        student_phone = request.form.get("student_phone")
        student_class = request.form.get("student_class")
        student_mail = request.form.get("student_mail")
        student_birtday = request.form.get("student_birtday")
        student_episode = request.form.get("student_episode")
        datas= {"student_name":student_name,"student_surname":student_surname,"student_phone":student_phone,"student_class":student_class,"student_mail":student_mail,"student_birtday":student_birtday,"student_episode":student_episode}
        sql_connect.Mysql_first(datas).student_register()
        return render_template("deneme1.html",total=datas)
    else:
        return render_template("deneme1.html")
# if __name__ == "__main__" :
#     app.run(debug=True)

###     STUDENT DELETE

@app.route("/student_delete",methods = ["GET","POST"])
def student_delete():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        # student_name = request.form.get("student_name")
        datas= {"student_id":student_id}
        sql_connect.Mysql_first(datas).student_delete()
        return render_template("deneme1.html")
    else:
        return render_template("deneme1.html")
# if __name__ == "__main__" :
#     app.run(debug=True)
    
###    STUDENT UPDATE   

@app.route("/student_update",methods = ["GET","POST"])
def student_update():
    if request.method == "POST":
        student_name = request.form.get("student_name")
        student_id = request.form.get("student_id")
        datas= {"student_name":student_name,"student_id":student_id}
        sql_connect.Mysql_first(datas).student_update()
        return render_template("deneme1.html",appealstudentupdate=student_name ) 
    else:
        return render_template("deneme1.html")
# if __name__ == "__main__" :
#     app.run(debug=True)

###     TEACHER API

@app.route("/teacher_register",methods = ["GET","POST"])
def teacher_register():
    if request.method == "POST":
        print("istek ulaştı")
        teacher_name = request.form.get("teacher_name")
        teacher_surname = request.form.get("teacher_surname")
        teacher_title = request.form.get("teacher_title")
        teacher_phone = request.form.get("teacher_phone")
        teacher_branch = request.form.get("teacher_branch")
        datas = {"teacher_name":teacher_name,"teacher_surname":teacher_surname,"teacher_title":teacher_title,"teacher_phone":teacher_phone,"teacher_branch":teacher_branch}
        sql_connect.Mysql_first(datas).teacher_register()
        return render_template("deneme1.html", appealteacherregister=teacher_name, teachername=teacher_name )
    else:
        return render_template("deneme1.html")
# if __name__ == "__main__" :
#     app.run(debug=True)



###     TEACHER UPDATE

@app.route("/teacher_update",methods = ["GET","POST"])
def teacher_update():
    if request.method == "POST":
        teacher_name = request.form.get("teacher_name")
        teacher_id = request.form.get("teacher_id")
        datas= {"teacher_name":teacher_name,"teacher_id":teacher_id}
        sql_connect.Mysql_first(datas).teacher_update()
        return render_template("deneme1.html", appealteacherupdate=teacher_name)
    else:
        return render_template("deneme1.html")
# if __name__ == "__main__" :
#     app.run(debug=True)

###     TEACHER DELETE

@app.route("/teacher_delete",methods = ["GET","POST"])
def teacher_delete():
    if request.method == "POST":
        teacher_id = request.form.get("teacher_id")
        datas= {"teacher_id":teacher_id}
        print("gerçek api")
        sql_connect.Mysql_first(datas).teacher_delete()
        return render_template("deneme1.html")
    else:
        return render_template("deneme1.html")
if __name__ == "__main__" :
    app.run(debug=True)



