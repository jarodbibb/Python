from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("user.html", red = 255, green = 255, blue = 255)

@app.route('/color', methods= ['POST'])
def color():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    return render_template("user.html", red = red, blue = blue, green = green)
app.run(debug = True)