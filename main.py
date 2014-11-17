from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"
	
@app.route('/send_data/<req>', methods=['GET', 'POST'])
def send_data(req):
    # if request.method == 'POST':
    data = request.stream.read().decode("utf-8")
    return '%s' % data

if __name__ == "__main__":
	app.run()

