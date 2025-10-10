from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "It is a easy project and I am making it complex, silly Priyanshu! DevOps Cloud Lab Running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
