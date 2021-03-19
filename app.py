from flask import Flask, jsonify,request

app = Flask(__name__);
@app.route("/workout", methods=["POST"])

def response():
    query = dict(request.form)['query']
    res = query + " Just curl bro"
    return jsonify({"response" : res})

if __name__=="__main__":
    app.run(host="0.0.0.0",)
