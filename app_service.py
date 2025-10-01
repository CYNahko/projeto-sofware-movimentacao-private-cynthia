import requests
import os

def validar_campos(data):
    campos_obrigatorios = ["cpf_comprador", "cpf_vendedor", "ticker", "quantidade"]
    for campo in campos_obrigatorios:
        if campo not in data:
            return f"Campo obrigatório '{campo}' não informado"
    return None

def calcular_valor(ticker, quantidade):
    url_base = os.getenv("STOCKS_URL")
    url = f"{url_base}/stocks/{ticker}"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            return None, f"Erro ao buscar ticker '{ticker}'"
        
        data = resp.json()
        valor_unitario = data.get("lastValue")
        return quantidade * valor_unitario, None
    except requests.RequestException as e:
        return None, f"Erro de conexão: {e}"

def criar_objeto_movimentacao(data, valor_total):
    return {
        "cpf_comprador": data["cpf_comprador"],
        "cpf_vendedor": data["cpf_vendedor"],
        "ticker": data["ticker"],
        "quantidade": data["quantidade"],
        "valor_movimentacao": valor_total
    }
