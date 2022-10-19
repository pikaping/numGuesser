from flask import Flask, flash, request, render_template

MIN_VALUE = 0
MAX_VALUE = 10000000000

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def guesser():
    if request.method == 'POST':
        data = request.form.get('numValue', -1)
        if type(data) == str:
            if data == "" or not data.isdigit():
                flash("Introduce un número, majo.", "error")
                return render_template("index.html")

        data = int(data)
        if (data < MIN_VALUE or data > MAX_VALUE):
            flash("El número es menor que %d o mayor que %d." % MIN_VALUE, MAX_VALUE, "error")
            return render_template("index.html")

        mxV = MAX_VALUE
        mnV = MIN_VALUE
        num = (MAX_VALUE + MIN_VALUE) / 2
        while(num != data):
            if data < num:
                mxV = num
            else:
                mnV = num
            num = (mxV + mnV) / 2

        flash("El número es: %d" % num, "info")
        return render_template("index.html")