import requests
from config.settings import API_URL, timeout, HEADERS
class AgenteTestador:
    def __init__(self):
        self.url = API_URL
        self.timeout = timeout
        self.headers = HEADERS

    def fazer_requisicao(self, endpoint):
        url_completa = self.url + endpoint
        resposta = requests.get(url_completa, headers=self.headers, timeout= self.timeout)
        return resposta
    
