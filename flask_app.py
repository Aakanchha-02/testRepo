from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/flask")
def flask_endpoint():
    return "Hello from Flask!"

if __name__ == "__main__":
    flask_app.run()