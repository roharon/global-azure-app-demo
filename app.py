from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>', methods=['GET'])
def home(name="World"):
    return render_template('home.html', name=name)

@app.route('/image')
def image():
    return render_template('img.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')