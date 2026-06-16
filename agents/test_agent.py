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


    
