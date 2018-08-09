from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from APP 1</br>Flask in a uWSGI Nginx Docker container with \
     Python 3.6 (from the example template)"


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
