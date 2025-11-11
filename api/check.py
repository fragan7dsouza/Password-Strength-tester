from flask import Flask, request, jsonify 
from password_checker import check_password_strength
from werkzeug.wrappers import Request, Response 

def handler(request: Request, response: Response):
    """
    Vercel handler function. Routes POST request to check() function.
    """
    if request.method == "POST":
        return check()

    response.status = 405
    response.headers["Content-Type"] = "application/json"
    response.end(jsonify({"error": "Method not allowed"}))
def check():
    app = Flask(__name__)
    with app.app_context():
        data = request.get_json(silent=True)
        password = data.get("password", "")
        
        result = check_password_strength(password)
        return jsonify(result)
