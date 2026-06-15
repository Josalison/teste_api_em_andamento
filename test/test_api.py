import pytest
from agents.test_agent import AgenteTestador
import json

def test_verificar_status_code_200():
    agente = AgenteTestador()
    resposta = agente.fazer_requisicao("/posts/1")
    assert resposta.status_code == 200

def test_verificar_status_jason():
    agente = AgenteTestador()
    resposta = agente.fazer_requisicao("/posts/1")
    dados = resposta.json()
    print(json.dumps(dados, indent=4))
    assert "title" in dados

def test_verificar_campo_userId():
    agente = AgenteTestador()
    resposta = agente.fazer_requisicao("/posts/1")
    dados = resposta.json()
    assert "userId" in dados
    