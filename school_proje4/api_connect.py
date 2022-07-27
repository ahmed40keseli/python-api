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
        json = request.json
        student_name = json["student_name"]
        student_surname = json["student_surname"]
        student_phone = json["student_phone"]
        student_class = json["student_class"]
        student_mail = json["student_mail"]
        student_birtday = json["student_birtday"]
        student_episode = json["student_episode"]
        datas= {"student_name":student_name,"student_surname":student_surname,"student_phone":student_phone,"student_class":student_class,"student_mail":student_mail,"student_birtday":student_birtday,"student_episode":student_episode}
        sql_connect.Mysql_first(datas).student_register()
        student_allreply={
            "message":"öğrenci kaydınız başarı ile gerçekleştirilmiştir",
            "code": 200
        }
        return student_allreply
    else:
        return "terminal isteğine yanıt"

###     STUDENT DELETE

@app.route("/student_delete",methods = ["GET","POST"])
def student_delete():
    if request.method == "POST":
        json = request.json
        student_id = json["student_id"]
        datas= {"student_id":student_id}
        sql_connect.Mysql_first(datas).student_delete()
        student_deletedic={
            "code":200,
            "message":"öğrenci kaydı silinmiştir"
        }
        return student_deletedic
    else:
        # return render_template("deneme1.html")
        return "çalışmadı"

###    STUDENT UPDATE   

@app.route("/student_update",methods = ["GET","POST"])
def student_update():
    if request.method == "POST":
        json = request.json
        student_name = json["student_name"]
        student_id = json["student_id"]
        datas= {"student_name":student_name,"student_id":student_id}
        sql_connect.Mysql_first(datas).student_update()
        student_updatedic = {
            "code":200,
            "message":"öğrenci güncelleştirmeniz başarı ile gerçekleşti"
        }
        return student_updatedic 
    else:
        return "çalışmadı"

###     TEACHER API

@app.route("/teacher_register",methods = ["GET","POST"])
def teacher_register():
    if request.method == "POST":
        json = request.json
        teacher_name = json["teacher_name"]
        teacher_surname = json["teacher_surname"]
        teacher_title = json["teacher_title"]
        teacher_phone = json["teacher_phone"]
        teacher_branch = json["teacher_branch"]
        print("name tanımlandı")
        datas = {"teacher_name":teacher_name,"teacher_surname":teacher_surname,"teacher_title":teacher_title,"teacher_phone":teacher_phone,"teacher_branch":teacher_branch}
        sql_connect.Mysql_first(datas).teacher_register()
        print("sql gönderildi")
        teacher_allreply = {
            "message":"öğretmen kaydınız başarı ile gerçekleşmiştir",
            "code":200
        }
        return teacher_allreply
    else:
        return "kayıt başarısız"

###     TEACHER UPDATE

@app.route("/teacher_update",methods = ["GET","POST"])
def teacher_update():
    if request.method == "POST":
        json = request.json
        teacher_name = json["teacher_name"]
        teacher_id = json["teacher_id"]
        datas= {"teacher_name":teacher_name,"teacher_id":teacher_id}
        sql_connect.Mysql_first(datas).teacher_update()
        return "çalıştı"
    else:
        return "çalışmadı"

###     TEACHER DELETE

@app.route("/teacher_delete",methods = ["GET","POST"])
def teacher_delete():
    if request.method == "POST":
        json = request.json
        teacher_id = json["teacher_id"]
        datas= {"teacher_id":teacher_id}
        sql_connect.Mysql_first(datas).teacher_delete()
        return "işlemi tamami"
    else:
        return "cevap"

###     ders alma

@app.route("/ders_alma",methods = ["GET","POST"])
def ders_alma():
    if request.method == "POST":
        json=request.json
        teacher_id = json["teacher_id"]
        teacher_name = json["teacher_name"]
        student_id = json["student_id"]
        student_name = json["student_name"]
        lesson_name = json["lesson_name"]
        datas = {"teacher_id":teacher_id,"teacher_name":teacher_name,"student_id":student_id,"student_name":student_name,"lesson_name":lesson_name}
        sql_connect.Mysql_first(datas).ders_alma()
        ders_alldic={
            "code":200,
            "message":"seçmiş olduğunuz ders alınmıştır"
        }
        return ders_alldic
    else:
        return "kayıt başarısız"

###     teacher sorgu

@app.route("/select_teacher",methods = ["GET","POST"])
def select_teacher():
    if request.method == "POST":
        json=request.json
        teacher_id = json["teacher_id"]
        teacher_name = json["teacher_name"]
        datas = {"teacher_id":teacher_id,"teacher_name":teacher_name}
        teacher_list=sql_connect.Mysql_first(datas).select_teacher()
        # print(f"tüm liste{teacher_list}")
        teacher_list2=[]

        for teacher in teacher_list:
            # print(f"sırayla elemanlar {teacher}")
            teacher_dic={}
            teacher_id=teacher[0]
            teacher_name=teacher[1]
            teacher_dic={"teacher_id":teacher_id,"teacher_name":teacher_name,}
            teacher_list2.append(teacher_dic)
        
        
        teacher_alldic={
            "data":teacher_list2,
            "message":"Öğrenci listesi hazırlanmıştır",
            "code":200
        }

        return teacher_alldic
    else:
        return "kayıt başarısız"

###     student sorgu

@app.route("/select_student",methods = ["GET","POST"])
def select_student():
    if request.method == "POST":
        json=request.json
        student_id = json["student_id"]
        student_name = json["student_name"]
        datas = {"student_id":student_id,"student_name":student_name}
        student_list=sql_connect.Mysql_first(datas).select_student()
        student_list2=[]
        for student in student_list:
            student_dic={}
            student_id=student[0]
            student_name=student[1]
            student_dic={"student_id":student_id,"student_name":student_name}
            student_list2.append(student_dic)
        
        student_dic2={
            "data":student_list2,
            "message":"Öğretmen liste hazırlandı",
            "code":200
            }

        return student_dic2
    else:
        return "kayıt başarısız"

###     ders sorgulama

@app.route("/select_all",methods = ["GET","POST"])
def select_all():
    if request.method == "POST":
        json=request.json
        teacher_id = json["teacher_id"]
        student_id = json["student_id"]
        lesson_name = json["lesson_name"]
        datas = {"teacher_id":teacher_id,"student_id":student_id,"lesson_name":lesson_name}
        all_list=sql_connect.Mysql_first(datas).select_all()
        all_list2 =[]
        print(all_list)
        for list_eleman in all_list:
            
            elements_dic = {}
            teacher_id = list_eleman[1]
            student_id = list_eleman[3]
            lesson_name = list_eleman[5]
            elements_dic={"teacher_id":teacher_id,"student_id":student_id,"lesson_name":lesson_name}
            all_list2.append(elements_dic)  
        
        all_dic={
            "data":all_list2,
            "message":"Öğretmen liste hazırlandı",
            "code":200
            }
        return all_dic
    else:
        return "kayıt başarısız"



if __name__ == "__main__" :
    app.run(debug=True)



