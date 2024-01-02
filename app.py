from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='K R Kaushik Kumar', usn='1BM20IS223', greeting='Hello, Flask!')

if __name__ == '__main__':
    app.run(debug=True)
