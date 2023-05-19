from flask import Flask,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='test'

mysql=MySQL(app)

'''
@app.route("/video")
def func():
    fid=cv.captureFace()
    cur=mysql.connection.cursor()
    cur.execute("CREATE table vishal(id int,faceid varchar);")
    cur.execute("Insert into vishal(id,faceid) VALUES(1,"+str(fid)+")")
    return "created"
'''

@app.route("/create")
def create():
    cur=mysql.connection.cursor()
    try:
        cur.execute("CREATE table data(id int,name varchar,pword varchar)")
        return "created"
    except:
        return "not created"

@app.route("/update",methods=['POST'])
def update():
    data=request.get_json()
    cur=mysql.connection.cursor()
    cur.execute("")
    return "updated"

@app.route("/check",methods=['POST'])
def check():
    data=request.get_json()
    if data:
        cur=mysql.connection.cursor()
        cur.execute("")
    return "found"

if __name__=="__main__":
    app.run()