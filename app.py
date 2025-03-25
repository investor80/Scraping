from flask import Flask, request, jsonify, render_template
import os
import requests
from bs4 import BeautifulSoup

# Configuração do Flask para procurar templates no diretório raiz
app = Flask(__name__, template_folder=os.path.abspath("."))

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({"error": f"Erro ao carregar o template: {str(e)}"}), 500

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        titles = {
            "h1": [h.get_text(strip=True) for h in soup.find_all('h1')],
            "h2": [h.get_text(strip=True) for h in soup.find_all('h2')],
            "h3": [h.get_text(strip=True) for h in soup.find_all('h3')]
        }

        return jsonify({"url": url, "titles": titles})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use a porta 5000 localmente ou pegue a variável de ambiente no Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
