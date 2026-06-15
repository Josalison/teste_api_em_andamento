import pytest
from agents.test_agent import AgenteTestador

def test_verificar_status_code_200():
    agente = AgenteTestador()
    resposta = agente.fazer_requisicao("/posts/1")
    assert resposta.status_code == 200