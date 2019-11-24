from flask import Flask

app = Flask(__name__, static_url_path='',static_folder='./')

@app.route('/')
def index():
    return "Hello from a_simpleServer.py"


@app.route('/book/<int:id>')
def getbook(id):
    return "You Want Book " + str(id)

if __name__ =='__main__':
    app.run(debug=True)
    