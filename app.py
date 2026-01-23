from flask import Flask
from app import add 

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def home():
    //What the user will see in the browser
    result = add(10, 20)
    return f"<h1>Hello from the Dev Side!</h1><p>The calculation is: {result}</p>"

if __name__ == "__main__":
    #'0.0.0.0 means 'listen to everyone', not just local connections
    app.run(host='0.0.0.0', port=5000)
    
