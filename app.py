from flask import Flask,session
from flask import render_template
from flask import request,redirect,url_for,make_response,jsonify

from gothonweb import planisphere01
import os
from werkzeug.utils import secure_filename
import parser
app = Flask(__name__)
app.secret_key = '6ObDJtab/PzHuD4hhvs='


'''
@app.route('/')
def hello_world():
	greeting='world'
#    return "hello world!"
    #return f'hello,{greeting}!'
	return render_template("index.html", greeting=greeting)



@app.route('/hello',methods=['GET','POST'])
def index():
    
    name=request.args.get('name','Nobody')
    greet=request.args.get('greet','hello')
    if name:
       # greeting=f'hello,{name}'
        greeting=f'{greet},{name}'
    else:
        greeting='hello world'
    
    
    greeting='hello world'
    if request.method=='POST':
        name=request.form['name']
        greet=request.form['greet']
        greeting=f'{greet},{name}'
        return render_template('index.html',greeting=greeting)

    else:
        return render_template('hello_form.html')
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':

        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        image_data = open(upload_path, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/png'
        #return redirect(url_for('upload'))
        return response
    return render_template('upload.html')       
if __name__ == "__main__":
    app.run()
'''


@app.route('/login')
def  login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    #从session中获得登录的账号和密码，清除存储在session中的属性信息
    #此处代码有错误，请注意。。。。。。。。。。。
    #user=session.get('username')
    #pwd=session.get('password')
    session.pop('user_name',None)
    session.pop('password',None)
    return render_template('logout.html')


@app.route('/hello',methods=['GET','POST'])
def hello():
    return render_template('hello_form.html')


@app.route("/")
def index():
    # this is used to "setup" the session with starting value
    session['room_name'] = planisphere01.START
    return redirect(url_for("index02"))


@app.route('/index02',methods=['GET','POST'])
def index02():
    if request.method=='GET':
        li=[planisphere01.START,planisphere01.SECOND,
        planisphere01.THIRD,planisphere01.FOURTH]

        #利用session获得用户名和密码session.getAttribute(“username”) 
        name=session.get('user_name')
        return render_template('index02.html',li=li,name=name)
    elif request.method=="POST":
        action=request.form.get('action')
        if action:
            session['room_name']=action
            return redirect(url_for('game'))
        else:
            #保存登录信息，用户名和密码，用session设置固定属性
            #session.setAttribute("name", "iverson");session.removeAttribute("name");
            username=request.form.get('name')
            password=request.form.get('password')
            #session['user_name']=username
            #session['password']=password
            #把用户信息存贮在session属性中
            session['user_name']=username
            session['password']=password
            return redirect(url_for('index02'))

@app.route('/change',methods=["GET","POST"])   # index02中提交form可以链接到此处
def change():
    if request.method=="POST":
        action=request.form.get('action')

        session['room_name']=action
        return redirect(url_for('game'))


@app.route('/help')
def help():
    a=planisphere01.central.paths
    a1=planisphere01.escape.paths
    #a2=planisphere01.generic_death.paths
    a3=planisphere01.laser.paths
    a4=planisphere01.the.paths
    # a5=planisphere01.the_end_loser.paths
    # a6=planisphere01.the_end_winner.paths

    li={}
    
    for k,v in a.items(): 
        li[k]=v.name
        
        print('k的制',k,'value值',v.name)
    for k,v in a1.items():
        li[k]=v.name
    for k,v in a3.items():
        li[k]=v.name
    for k,v in a4.items():
        li[k]=v.name
    return render_template('help_info.html',li=li)


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere01.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do you need it?'
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere01.load_room(room_name)

            #写词汇解析代码
            try:
                if type(int(action))!=int:
                    myword=parser.convert_word(action)
                    print('词汇解析完后的代码',myword)
                    next_room = room.go(myword)
                else:
                    next_room=room.go(action)
            except Exception as e:
                print('error>>>>>>>>>>',e)
                myword=parser.convert_word(action)
                print('词汇解析完后的代码',myword)
                next_room = room.go(myword)

                
            if not next_room:
                session['room_name'] = planisphere01.name_room(room)
            else:
                session['room_name'] = planisphere01.name_room(next_room)

        return redirect(url_for("game"))


# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET

if __name__ == "__main__":
   

    app.run()



