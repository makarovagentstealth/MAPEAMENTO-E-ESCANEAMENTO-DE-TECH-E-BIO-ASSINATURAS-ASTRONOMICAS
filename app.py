from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/celestial_data')
def celestial_data():
    # Simulação de dados da API do James Webb
    # Em uma implementação real, você faria uma requisição à API aqui
    # response = requests.get('URL_DA_API_DO_JAMES_WEBB')
    # data = response.json()

    # Dados simulados
    data = {
        'object': 'MAPEAMENTO DE TECH E BIO ASSINATURA COM O PRIVILEGIO DE SETAGEM DO INTERCEPT BURP SUITE PROFISSIONAL E O PROTOCOLO INTERNO E EXTERNO DO OS E A API DO JAMES WEBB DA NASA',
        'approximationValue': round(random.uniform(-100, 100), 2)  # Valor entre -100 e +100
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)