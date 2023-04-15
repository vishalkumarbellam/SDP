from flask import Flask,request
import CaptureVideo as cv

app=Flask(__name__)

@app.route("/video")
def func():
    cf=cv.captureFace()
    d={'a':cf[0],'b':cf[1]}
    return d

if __name__=="__main__":
    app.run()