from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/helloagain')
def hello_again():
	return 'hello again'

if __name__ == '__main__':
	app.run()

