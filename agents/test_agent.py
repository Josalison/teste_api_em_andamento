import requests
import os
import time
from google import genai
from dotenv import load_dotenv
from config.settings import API_URL, timeout, HEADERS

class AgenteTestador:
    def __init__(self):
        self.url = API_URL
        self.timeout = timeout
        self.headers = HEADERS
        load_dotenv()
        self.cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def get(self, endpoint):
        url_completa = self.url + endpoint
        resposta = requests.get(url_completa, headers=self.headers, timeout=self.timeout)
        dados = resposta.json()
        prompt = f"""
        Você é um especialista em testes de API.
        Analise essa resposta de uma requisição GET:
        
        Dados: {dados}
        
        Verifique:
        - Os campos fazem sentido?
        - Os valores estão corretos?
        - Algo parece errado ou suspeito?
        
        Responda em português de forma clara e objetiva.
        """
        time.sleep(4)
        analise = self.cliente.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return resposta, analise.text