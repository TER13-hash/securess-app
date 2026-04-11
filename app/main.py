from flask import Flask, jsonify, request
import re

app = Flask(__name__)

ITEMS = []

def is_valid_name(name: str) -> bool:
    """Allow only alphanumeric names up to 64 chars."""
    return bool(re.match(r'^[a-zA-Z0-9 ]{1,64}$', name))

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/items', methods=['GET'])
def list_items():
    return jsonify({"items": ITEMS}), 200

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json(silent=True)
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    name = data['name']
    if not isinstance(name, str) or not is_valid_name(name):
        return jsonify({"error": "Invalid name"}), 422
    ITEMS.append(name)
    return jsonify({"added": name}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
