from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Привет, Соня и Макар'
app.run(port = 800)

