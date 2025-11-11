from flask import Flask, request, jsonify, render_template
from password_checker import check_password_strength

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
