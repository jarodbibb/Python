from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/color", methods=['POST'])
def create_color():
    r = request.form['r']
    g = request.form['g']
    b = request.form['b']
 
    return render_template('index.html', r =r, g = g, b=b
    )

app.run(debug=True)