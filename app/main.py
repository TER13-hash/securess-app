from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    if not data or "a" not in data or "b" not in data:
        return jsonify({"error": "Invalid input"}), 400

    try:
        a = float(data["a"])
        b = float(data["b"])
    except (ValueError, TypeError):
        return jsonify({"error": "Inputs must be numbers"}), 400

    return jsonify({"result": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
