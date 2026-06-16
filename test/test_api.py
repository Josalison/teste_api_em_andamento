import pytest
from agents.test_agent import AgenteTestador
import json

def test_get_com_ia():
    agente = AgenteTestador()
    resposta, analise = agente.get("/posts/1")
    print("\n🤖 Análise da IA:")
    print(analise)
    assert resposta.status_code == 200

