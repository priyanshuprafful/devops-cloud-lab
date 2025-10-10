from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Learning Github Actions , AWS,DOCKER,EKS , making a simple project from scratch using perplexity ,."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
