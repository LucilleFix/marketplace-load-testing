from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route('/api/orders', methods=['GET'])
def get_orders():
    time.sleep(random.uniform(0.1, 0.5))
    return jsonify({
        "orders": [
            {"id": 1, "sku": "SKU001", "qty": 2},
            {"id": 2, "sku": "SKU002", "qty": 1}
        ]
    })

@app.route('/api/products', methods=['GET'])
def get_products():
    query = request.args.get('search', '')
    time.sleep(random.uniform(0.2, 0.6))
    return jsonify({
        "products": [
            {"id": 101, "name": "Monitor", "price": 10000},
            {"id": 102, "name": "Keyboard", "price": 1500}
        ] if "mon" in query.lower() or query == "" else []
    })

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify({
        "stocks": [
            {"sku": "SKU001", "qty": 50},
            {"sku": "SKU002", "qty": 30}
        ]
    })

@app.route('/api/prices', methods=['POST'])
def update_prices():
    data = request.json
    time.sleep(random.uniform(0.1, 0.4))
    if not data or "sku" not in data or "price" not in data:
        return jsonify({"error": "Bad request"}), 400
    return jsonify({"message": f"Price for {data['sku']} updated to {data['price']}"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
