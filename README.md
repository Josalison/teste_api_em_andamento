# 🤖 Agente de Testes de API com IA

Projeto de automação de testes de API usando Python, Pytest e Google Gemini.

## 🛠️ Tecnologias
- Python
- Pytest
- Playwright
- Requests
- Google Gemini AI

## 📁 Estrutura
```
projeto_teste/
├── agents/        → agente com IA integrada
├── config/        → configurações da API
├── reports/       → relatórios dos testes
└── test/          → testes automatizados
```

## ⚙️ Como rodar

### 1. Clonar o projeto
```bash
git clone https://github.com/SEU_USUARIO/projeto_teste.git
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar a chave do Gemini
Crie um arquivo `.env` na raiz:
```
GEMINI_API_KEY=sua_chave_aqui
```

### 5. Rodar os testes
```bash
pytest test/ -v
```

## 🚧 Status
Projeto em desenvolvimento.
