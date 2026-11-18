from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route("/")
def home():
    return jsonify(mensagem="Olá, Docker!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify(resultado=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)