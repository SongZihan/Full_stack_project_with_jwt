from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index_page():
    return render_template('index.html')


@app.route('/get_something',methods=["GET"])
def hello_world():
    """
    This is a test api.
    :return: Dict
    """
    msg = 'Hello Vue.js'
    data = 'This is data'
    return jsonify({"msg":msg,"data":data})





if __name__ == "__main__":
    app.run(host="localhost")
