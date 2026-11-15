import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({
        "mensagem": "Hello World! Aplicação Flask da Livraria O2O online no Azure App Services!",
        "status": "online",
        "exercicio": "9.3 - Flask e Nuvem"
    }), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=porta)
