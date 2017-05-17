from flask import Flask
app = Flask(__name__)

# Basic route & corresponding request handler
@app.route("/")
def main():
    return "Welcome!"

# check , if the executed file is the main programm and run the app
if __name__ == "__main__":
    app.run()
