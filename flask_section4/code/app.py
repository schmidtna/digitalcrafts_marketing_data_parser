from flask_jwt import JWT, jwt_required
from flask import Flask, request
from flask_restful import Resource, Api

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'nick'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

# api works with resources, every resource needs to be a class:
class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.  ".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # 201 is created status

    def delete(self, name):
        global items # without this it iterates over the local items list which is empty
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=8080, debug=True)