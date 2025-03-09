# Web Scraper Simples

Este é um scraper simples que coleta títulos (h1, h2, h3) de uma página da web e os exibe na interface web.

## Como Implantar no Render

1. Faça um fork deste repositório e clone para o seu GitHub.
2. Vá para [Render.com](https://render.com/).
3. Crie um novo **Web Service** e conecte o repositório.
4. Configure:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Port**: 5000
5. Aguarde a implantação e acesse a URL gerada!

## Como Usar

- Acesse a página principal.
- Insira uma URL e clique no botão para fazer o scraping.
- Os títulos encontrados serão exibidos na tela.
