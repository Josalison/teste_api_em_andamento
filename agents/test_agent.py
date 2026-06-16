import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os
from config.settings import API_URL, timeout, HEADERS

class AgenteTestador:
    def __init__(self):
        self.url = API_URL
        self.timeout = timeout
        self.headers = HEADERS
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.modelo = genai.GenerativeModel("gemini-1.5-flash")

    def get(self, endpoint):
        url_completa = self.url + endpoint
        resposta = requests.get(url_completa, headers=self.headers, timeout=self.timeout)
        dados = resposta.json()
        promt = f"""
        Você é um especialista em testes de API.
        Analise essa resposta de uma requisição GET:
        
        Dados: {dados}
        
        Verifique:
        - Os campos fazem sentido?
        - Os valores estão corretos?
        - Algo parece errado ou suspeito?
        
        Responda em português de forma clara e objetiva.
        """
        analise = self.modelo.generate_content(promt)
        return resposta, analise.text
    


    
