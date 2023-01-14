from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from EvalVisitor import EvalVisitor, get_funcs
from flask import Flask, render_template, jsonify, request, url_for

app = Flask(__name__)

ios = []
fxs = []

def process_stream(input_stream):
    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root() 
    visitor = EvalVisitor()
    return visitor.visit(tree)

process_stream(FileStream("std.funx"))
fxs = get_funcs()

@app.route("/")
def base():
    return render_template('base.html', output=ios, functions=fxs)

@app.route("/input", methods=["POST"])
def input():
    text = request.get_json()['input']
    out = process_stream(InputStream(text))
    if str(out) == "None":
        out = ""
    ios.append((text, str(out)))
    return jsonify(ios)

@app.route("/fxs", methods=["GET"])
def functions():
    funcs = get_funcs();
    return jsonify(funcs)