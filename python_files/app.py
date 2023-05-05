from flask import Flask,request
from flask_mysqldb import MySQL
import CaptureVideo as cv

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='test'

mysql=MySQL(app)

@app.route("/video")
def func():
    #cf=cv.captureFace()
    cur=mysql.connection.cursor()
    cur.execute("CREATE table vishal(id int);")
    return "created"

if __name__=="__main__":
    app.run()