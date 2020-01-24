# wsgi.py
from flask import Flask, jsonify, request, make_response, abort
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    {'id': 3 , 'name': 'toto.tv'}
]

def product_exist(id):
    if id in PRODUCTS:
        return True
    else :
        return False

class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id

ID = Counter()


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def get_products():

    make_response(jsonify(PRODUCTS), 200)

@app.route('/api/v1/products/<int:id>', methods=['GET', 'POST', 'DELETE'])
def product(id):
    if not product_exist(id):
        abort(404)

    if request.method == 'GET':
        make_response(jsonify(PRODUCTS[id]),200)

    if request.method == 'POST':
        return add_product(id)

    if request.method == 'DELETE':
        make_response("",201)

@app.route('/api/v1/products/<int:id>', methods=['POST'])
def product(id):


