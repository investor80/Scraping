from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
