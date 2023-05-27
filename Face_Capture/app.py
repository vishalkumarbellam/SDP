from flask import Flask
import FaceRecognition as fm

app = Flask(__name__)

@app.route("/FaceRecognition/<id>")
def capture_face(id):
    return fm.main(id)

if __name__ == "__main__":
    app.run()