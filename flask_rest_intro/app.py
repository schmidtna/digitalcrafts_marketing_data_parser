from flask import Flask, jsonify, request

app = Flask(__name__)
# __name__ is a special py variable that gives each file a unique name
# flask needs to know where the app is running, which is what this is for



# this defines what type of requests flask will expect
# this would be the homepage of a URL
# @app.route by default is a get request
# @app.route("/")
# def home():
#     return "Hello, world!"

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]



# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        else:
            return jsonify({"message": "store not found"})
    #iterate over stores, return matching stores

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})
    #json needs a dict, but we're passin in a list, so we turn our list into a dict

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
        else:
            return jsonify({"message": "store not found"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store['items']})
        else:
            return jsonify({"message": "store not found"})


app.run(port=8080)
