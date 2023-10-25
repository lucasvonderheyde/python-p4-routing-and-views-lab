
from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index_route():
    return make_response('<h1>Python Operations with Flask Routing and Views</h1>', 200)

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return make_response(parameter, 200)

@app.route('/count/<parameter>')
def count_route(parameter):
    count = ''
    for i in range(0, int(parameter)):
        count += str(i)
        count += "\n"
    print(count)
    return make_response(count, 200)

@app.route('/math/<number1>/<operation>/<number2>')
def math_route(number1, operation, number2):
    result = 0
    print(operation)
    if operation == '*':
        result = int(number1) * int(number2)
    elif operation == '+':
        result = int(number1) + int(number2)
    elif operation == '-':
         result = int(number1) - int(number2)
    elif operation == '/':
        result = int(number1) / int(number2)
    elif operation == 'div':
        result = int(number1) / int(number2)
    
    return make_response(str(result), 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
