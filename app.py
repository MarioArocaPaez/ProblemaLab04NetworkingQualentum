from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de Qualentum"})

@app.route('/status')
def status():
    return jsonify({"status": "OK", "message": "El servidor está funcionando correctamente."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
