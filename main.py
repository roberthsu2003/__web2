from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    print(f"request的attribute method:{request.method}")
    print(f"request的property mimetype:{request.mimetype_params}")
    return render_template('index.html')