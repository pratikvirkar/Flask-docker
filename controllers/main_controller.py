from config.app_config import *


@app.route('/')         #http://localhost:5000/
@app.route('/index')    #http://localhost:5000/index
def welcome_to_the_application():
    #return "Welcome to the flask sample Application..!"
    return render_template('index.html')


@app.route('/login',methods=['POST','GET'])
def user_login():

    if request.method == 'GET':
        formdata = request.args     # request url
        print('GET METHOD INVOKED')
    else:
        formdata = request.form         #request body
        print('POST METHOD INVOKED..')

    uname = formdata.get('username')
    pwd = formdata.get('password')
    if uname in ["yogesh","akshay","amit"] and pwd == "yogesh123":
        return render_template('home.html',username = uname)
    else:
        return render_template('index.html',message = "Invalid Credentials..!")
