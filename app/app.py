from flask import Flask, render_template, request
from config import app

app = Flask(__name__)

def ascii_func(string):
    line = [chr(ord(string[i]) - 1) for i in range(len(string))]
    text = (''.join(line))
    print(text)
    return text

@app.route('/', methods=('GET', 'POST'))
def index():
    result = ''
    if request.method == "POST":
        data = str(request.form.get("Data"))
        result = ascii_func(data)
    return render_template('index.html', result=result)
 
if __name__== '__main__':
    app.run()
