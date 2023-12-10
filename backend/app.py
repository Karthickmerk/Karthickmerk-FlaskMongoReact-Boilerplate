from flask import Flask, jsonify
# from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient("mongodb://mongo:27017/mydatabase")
# db = client.mydatabase

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, world!"})

@app.route("/users", methods=["GET"])
def get_users():
    return 'users'

if __name__ == "__main__":
    app.run(debug=True)

