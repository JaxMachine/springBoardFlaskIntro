# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

@app.route("/add")
def route_add():
    """Add a and b together"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)


@app.route("/sub")
def route_sub():
    """Subtract b from a together"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def route_mult():
    """Mulitply a by b together"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def route_div():
    """Divide a by b together"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)


operators = {
    "add": add,
    "sub" : sub,
    "mult": mult,
    "div": div
    }

@app.route("/math/<oper>")
def route_math(oper):
    """Do the math operation indicated but the route"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a,b)

    return str(result)