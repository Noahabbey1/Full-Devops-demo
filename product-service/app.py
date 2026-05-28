from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def products():
    return jsonify({
        "message": [
            "Laptop",
            "Phone",
            "keyboard"
        ]
    })

if __name__ == '__main__':
    app.run(port=5002, debug=True)